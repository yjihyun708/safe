import os
import time

import pydirectinput as pag  # pip install pydirectinput
from flask import Flask, redirect, render_template, request, session, url_for

# from pyngrok import ngrok


app = Flask(__name__)
app.secret_key = 'secure-key'

# 간단한 사용자 데이터베이스
user_db = {
    'teacher1': {'password': '1234', 'model_key': 'abcModelKey123'}
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = user_db.get(username)
    if user and user['password'] == password:
        session['username'] = username
        return redirect(url_for('main'))
    return '로그인 실패. <a href=\"/\">다시 시도</a>'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/main')
def main():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('main.html', username=session['username'], model_key=user_db[session['username']]['model_key'])

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
