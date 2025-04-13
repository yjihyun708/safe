import os
import time

import pydirectinput as pag  # pip install pydirectinput
from flask import Flask, redirect, render_template, request, session, url_for

# from pyngrok import ngrok


app = Flask(__name__)
app.secret_key = 'secure-key'

# 간단한 사용자 데이터베이스 (기존)
user_db = {
    'teacher1': {'password': '1234', 'model_key': 'abcModelKey123'}
}

@app.route('/')
def home():
    # 세션에 학생 정보(username)이 있으면 메인 페이지로 리다이렉트
    if 'username' in session:
        return redirect(url_for('main'))
    # 학생 정보 입력 페이지 표시 (login.html → 학생 정보 입력 페이지)
    return render_template('login.html')

# 학생 정보 입력을 처리하는 라우트 추가
@app.route('/student_info', methods=['POST'])
def student_info():
    # 폼으로부터 학년과 이름 정보를 받아 세션에 저장
    grade = request.form.get('grade')
    name = request.form.get('name')
    if not grade or not name:
        return "모든 필드를 입력해주세요", 400
    session['username'] = name      # 메인 페이지에서는 'username'이 필요하므로 name을 저장합니다.
    session['grade'] = grade        # 추가로 학년 정보도 저장할 수 있습니다.
    return redirect(url_for('main'))

@app.route('/login', methods=['POST'])
def login():
    # 기존 로그인 로직은 필요 없다면 삭제하거나 별도로 유지합니다.
    username = request.form['username']
    password = request.form['password']
    user = user_db.get(username)
    if user and user['password'] == password:
        session['username'] = username
        return redirect(url_for('main'))
    return '로그인 실패. <a href="/">다시 시도</a>'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/main')
def main():
    if 'username' not in session:
        return redirect(url_for('home'))
    # 메인 페이지에 학생 정보 (예: username, 학년) 및 모델 키 전달
    return render_template('main.html', username=session['username'], 
                           model_key=user_db.get(session.get('username'), {}).get('model_key', 'defaultModelKey'))

@app.route('/save_model', methods=['POST'])
def save_model():
    if 'username' in session:
        model_key = request.form['model_key']
        user_db[session['username']]['model_key'] = model_key
        return f"모델 키가 저장되었습니다: {model_key}"
    return "로그인 필요"

@app.route('/action', methods=['GET'])
def action():
    index = request.args.get('index')
    print(f"동작 인식됨: {index}")
    # print(f"[INFO] Received index: {index}")
    # time.sleep(2)  # 포커스 전환 시간

    if index == '1':
        pag.press('up')
    elif index == '2':
        pag.press('down')
    elif index == '3':
        pag.press('right')
    elif index == '4':
        pag.press('left')
    else:
        return "Invalid index", 400

    return "ok"
    # return f"Action {index} executed", 200

# if __name__ == '__main__':
#     public_url = ngrok.connect(5000)
#     print(f"\n🟢 외부 접속 주소: {public_url}\n")
#     os.system(f"start {public_url}")
#     app.run(port=5000)

# @app.before_first_request
# def setup_ngrok():
#     public_url = ngrok.connect(5001)
#     print(f"🔗 ngrok 외부 주소: {public_url}")

if __name__ == "__main__":
    app.run(port=5001)
    
    
######### ngrok 테스트 ###########
# if __name__ == '__main__':
#     # 포트 8080으로 Flask 서버 실행
#     # (host='0.0.0.0' 설정하면 외부 접속 허용)
#     app.run(host='0.0.0.0', port=8080, debug=True)
