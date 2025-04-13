import os
import time

import pydirectinput as pag  # pip install pydirectinput
from flask import Flask, render_template, request

# from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['GET'])
def action():
    index = request.args.get('index')
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

    return f"Action {index} executed", 200

# if __name__ == '__main__':
#     public_url = ngrok.connect(5000)
#     print(f"\n🟢 외부 접속 주소: {public_url}\n")
#     os.system(f"start {public_url}")
#     app.run(port=5000)

# if __name__ == "__main__":
#   app.run(port=5001)
if __name__ == '__main__':
    # 포트 8080으로 Flask 서버 실행
    # (host='0.0.0.0' 설정하면 외부 접속 허용)
    app.run(host='0.0.0.0', port=8080, debug=True)
