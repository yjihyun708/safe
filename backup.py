# ################################################3
# ## ngrok은 가능한데, 키보드 제어가 안됨
# ###################################################3
# #######################################################################3
# # Flask와 flask-ngrok 라이브러리를 활용하여 교사 컴퓨터에서 서버를 실행할 때 자동으로 ngrok 임시 URL을 생성하는 예제 코드
# # 이 코드를 실행하면 교사 컴퓨터에서 ngrok 터널이 열리고, 
# # 생성된 URL을 학생들에게 배포하여 학생들의 컴퓨터에서는 별도의 VS Code 설치나 터미널 명령 없이 웹브라우저로 접근할 수 있습니다.
# # 패키지 먼저 설치하기
# # pip install flask flask-ngrok

# # -*- coding: utf-8 -*-
# """
# 이 코드는 Flask와 flask-ngrok을 이용해 교사 컴퓨터에서 서버를 실행하면서
# ngrok을 통해 외부 접근 가능한 임시 URL을 생성합니다.
# 학생들이 웹페이지를 통해 방향키 이벤트(index 값)를 전송하면, keyboard 라이브러리로 키 입력이 시뮬레이션됩니다.
# """
# import time  # 추가: time 모듈 import

# import pydirectinput as pag
# from flask import Flask, jsonify, make_response, render_template, request

# # Windows 사용자라면 아래 주석을 해제하고 사용하세요.
# # import pydirectinput as pag
# # MAC OS
# # import pyautogui as pag 

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def main():
#     # templates 폴더의 index.html 파일을 렌더링합니다.
#     return render_template('index.html')

# @app.route("/action", methods=["GET"])
# def action():
#     index = request.args.get('index')
#     print("index : " + index)
    
#     time.sleep(3)  # 3초 후에 실행되므로, 테스트할 창으로 포커스를 옮깁니다.
#     pag.press('right')
    
# #     # index 값에 따라 방향키 입력을 발생시킵니다.
# #     if index == '1':
# #         pag.press('up')
# #     elif index == '2':
# #         pag.press('down')
# #     elif index == '3':
# #         pag.press('right')
# #     elif index == '4':
# #         pag.press('left')

#     return make_response(jsonify({"status number": 200}), 200)

# if __name__ == '__main__':
#     # 포트 8080으로 Flask 서버 실행
#     # (host='0.0.0.0' 설정하면 외부 접속 허용)
#     app.run(host='0.0.0.0', port=8080, debug=True)







# #######################################################################
# # Flask와 flask-ngrok 라이브러리를 활용하여 교사 컴퓨터에서 서버를 실행할 때 자동으로 ngrok 임시 URL을 생성하는 예제 코드
# # 이 코드를 실행하면 교사 컴퓨터에서 ngrok 터널이 열리고, 
# # 생성된 URL을 학생들에게 배포하여 학생들의 컴퓨터에서는 별도의 VS Code 설치나 터미널 명령 없이 웹브라우저로 접근할 수 있습니다.
# # 패키지 먼저 설치하기
# # pip install flask flask-ngrok
# #######################################################################

# # -*- coding: utf-8 -*-
# """
# 이 코드는 Flask와 flask-ngrok을 이용해 교사 컴퓨터에서 서버를 실행하면서
# ngrok을 통해 외부 접근 가능한 임시 URL을 생성합니다.
# 학생들이 웹페이지를 통해 방향키 이벤트(index 값)를 전송하면, keyboard 라이브러리로 키 입력이 시뮬레이션됩니다.
# """

# import keyboard  # 키보드 이벤트 전송 (pip install keyboard)
# from flask import Flask, jsonify, make_response, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     # templates 폴더 내 index.html 파일을 렌더링합니다.
#     return render_template("index.html")

# @app.route("/action", methods=["GET"])
# def action():
#     index = request.args.get('index')
#     print("index :", index)

#     # index 값에 따라 방향키 이벤트를 발생시킵니다.
#     if index == '1':
#         keyboard.send('up')    # ↑ (up) 방향키 전송
#     elif index == '2':
#         keyboard.send('down')  # ↓ (down) 방향키 전송
#     elif index == '3':
#         keyboard.send('right') # → (right) 방향키 전송
#     elif index == '4':
#         keyboard.send('left')  # ← (left) 방향키 전송

#     return make_response(jsonify({"status number": 200}), 200)

# if __name__ == '__main__':
#     # 포트 8080으로 Flask 서버 실행
#     # (host='0.0.0.0' 설정하면 외부 접속 허용)
#     app.run(host='0.0.0.0', port=8080, debug=True)









# ################# ngrok - 실패. 설치가 안됨. windows 보안에 걸림 #################
# # pydirectinput 대신 keyboard 모듈을 사용하여 물리 키보드 제어를 구현한 코드입니다.
# # ngrok를 사용하여 외부에서도 해당 Flask 앱에 접근할 수 있도록 설정되어 있으며, /action 엔드포인트를 호출하면 키보드의 ↑(up), ↓(down), →(right), ←(left) 방향키가 실제로 전송
# # 주의:
# # keyboard 모듈은 일부 운영체제(주로 Windows)에서 관리자 권한이 필요할 수 있습니다.
# # 외부 접속 시 키 입력 전송 경로와 보안을 충분히 고려하시기 바랍니다.
# ####################################################################################

# import ctypes
# import os
# import sys


# # 관리자 권한(elevated privileges) 확인 및 재실행
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if not is_admin():
#     # 관리자 권한으로 재실행 (runas)
#     print("관리자 권한이 필요합니다. 관리자 권한으로 재실행합니다.")
#     ctypes.windll.shell32.ShellExecuteW(
#         None, "runas", sys.executable, " ".join(sys.argv), None, 1
#     )
#     sys.exit()

# # 관리자 권한 획득 후 실제 코드 실행
# import keyboard  # 실제 키보드 제어 모듈
# from flask import Flask, jsonify, make_response, render_template, request
# from pyngrok import ngrok  # ngrok 터널링 모듈

# # 필요 시 ngrok 수동 설치 경로 지정 (선택 사항)
# # os.environ["NGROK_PATH"] = r"C:\ngrok\ngrok.exe"

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def main():
#     return render_template('index.html')

# @app.route("/action", methods=["GET"])
# def action():
#     index = request.args.get('index')
#     print("index :", index)

#     if index == '1':
#         keyboard.send('up')    # ↑ 방향키 전송
#     elif index == '2':
#         keyboard.send('down')  # ↓ 방향키 전송
#     elif index == '3':
#         keyboard.send('right') # → 방향키 전송
#     elif index == '4':
#         keyboard.send('left')  # ← 방향키 전송

#     return make_response(jsonify({"status number": 200}), 200)

# if __name__ == "__main__":
#     port = 5001
#     # ngrok 터널을 "us" 리전으로 생성
#     public_url = ngrok.connect(port, region="us")
#     print(" * Public URL:", public_url)
#     app.run(port=port)








# ###################################################################################
# # pyngrok (Python NGrok 라이브러리)**를 활용하여 local Streamlit 앱을 외부에 노출하는 코드
# # Teachable Machine을 이용한 커스텀 컨트롤 HTML을 포함하며, 원본에서 물리 키보드 제어를 위한 pydirectinput 기능은 제거됨
# ###################################################################################

# ############ ngrok 설치 ############
# # 1. choco install ngrok
# # 2. ngrok config add-authtoken 2vcnEs3bMVWxJNVSF0piz2I83zR_6DeaHhtgg2VDG2U5BCEWx
# # 3. 임시 도메인 ngrok http http://localhost:8080

# ############ 코드 설명 ############
# # 1. pyngrok 터널 생성
# # 코드 시작부분에서 pyngrok을 사용해 Streamlit 기본 포트(8501)를 외부에 노출하는 터널을 생성합니다.

# # 2. Streamlit 앱 설정
# # Streamlit 페이지 설정 및 기본 타이틀, 설명을 작성합니다.

# # 3. HTML/JavaScript 삽입
# # 원본 HTML 코드를 수정하여 pydirectinput 관련 코드는 제거한 후, Teachable Machine 모델을 사용해 웹캠과 예측 결과를 출력하는 기능을 포함합니다.

# # 4. 스트림릿 컴포넌트
# # streamlit.components.v1의 components.html 함수를 사용하여 HTML 코드를 앱에 삽입합니다.
# ###################################################################################

# # 1. 필수 라이브러리 설치
# # pip install streamlit pyngrok

# # 코드 실행
# # streamlit run app.py
# ###################################################################################

# import streamlit as st
# import streamlit.components.v1 as components
# from pyngrok import ngrok

# # ngrok 터널 생성 (Streamlit 기본 포트: 8501)
# public_url = ngrok.connect(8501)
# st.write("ngrok URL:", public_url)

# # 페이지 설정
# st.set_page_config(page_title="Safe Streamlit App", layout="wide")
# st.title("Safe Streamlit 앱")
# st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# # HTML 코드: pydirectinput 기능 제거 후 Teachable Machine 컨트롤 코드 사용
# html_code = """
# <html>
#   <head>
#     <meta charset="UTF-8">
#     <style>
#       body { font-family: Arial, sans-serif; }
#       #action-output { font-size: 24px; font-weight: bold; color: blue; margin-top: 10px; }
#     </style>
#   </head>
#   <body>
#     <div>Custom control based on Teachable Machine</div>
#     <input type="text" id="tm_model_key" value="wef1yJup2">
#     <button type="button" onclick="init()">Load Model</button>
#     <div><canvas id="canvas"></canvas></div>
#     <div id="label-container"></div>
#     <!-- 추가: 인식된 동작 결과 표시 영역 -->
#     <div id="action-output">인식된 동작: None</div>
#     <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
#     <script type="text/javascript">
#       let model, webcam, ctx, labelContainer, maxPredictions;

#       // 모델 및 웹캠 초기화 함수
#       async function init() {
#           let tm_model_key = document.getElementById("tm_model_key").value;
#           let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
#           let modelURL = URL + "model.json";
#           let metadataURL = URL + "metadata.json";

#           // 모델과 메타데이터 로드
#           model = await tmPose.load(modelURL, metadataURL);
#           maxPredictions = model.getTotalClasses();

#           // 웹캠 설정
#           const size = 200;
#           const flip = true; // 좌우 반전 여부
#           webcam = new tmPose.Webcam(size, size, flip);
#           await webcam.setup();
#           await webcam.play();
#           window.requestAnimationFrame(loop);

#           // canvas 및 라벨 컨테이너 초기화
#           const canvas = document.getElementById("canvas");
#           canvas.width = size;
#           canvas.height = size;
#           ctx = canvas.getContext("2d");
#           labelContainer = document.getElementById("label-container");
#           for (let i = 0; i < maxPredictions; i++) {
#               labelContainer.appendChild(document.createElement("div"));
#           }
#       }

#       // 반복 함수: 웹캠 프레임 업데이트 및 예측 수행
#       async function loop(timestamp) {
#           webcam.update();
#           await predict();
#           window.requestAnimationFrame(loop);
#       }

#       var prev_action_time = new Date().getTime();
#       var cur_action_time = new Date().getTime();

#       // 예측 함수
#       async function predict() {
#           const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
#           const prediction = await model.predict(posenetOutput);

#           let action_index = -1;
#           let action_prop = -1;
#           // 예측된 클래스 중 확률이 가장 높은 인덱스 선택
#           for (let i = 0; i < maxPredictions; i++) {
#               const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
#               if (prediction[i].probability > action_prop) {
#                   action_prop = prediction[i].probability;
#                   action_index = i;
#               }
#               labelContainer.childNodes[i].innerHTML = classPrediction;
#           }

#           cur_action_time = new Date().getTime();
#           let diff_time = cur_action_time - prev_action_time;
#           if (diff_time > 200) {
#               prev_action_time = cur_action_time;
#               sendAction(action_index);
#           }
#           drawPose(pose);
#       }

#       // 인식된 action_index에 따른 동작 출력
#       function sendAction(action_index) {
#           let actionName = "";
#           if (action_index === 0) {
#               actionName = "Up (위)";
#           } else if (action_index === 1) {
#               actionName = "Down (아래)";
#           } else if (action_index === 2) {
#               actionName = "Right (오른쪽)";
#           } else if (action_index === 3) {
#               actionName = "Left (왼쪽)";
#           } else {
#               actionName = "Unknown Action";
#           }
#           document.getElementById("action-output").innerHTML = "인식된 동작: " + actionName;
#           console.log("Detected action index:", action_index, actionName);
#       }

#       // 포즈 그리기 함수
#       function drawPose(pose) {
#           if (webcam.canvas) {
#               ctx.drawImage(webcam.canvas, 0, 0);
#               if (pose) {
#                   const minPartConfidence = 0.5;
#                   tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
#                   tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
#               }
#           }
#       }
#     </script>
#   </body>
# </html>
# """

# # 스트림릿 컴포넌트를 이용해 HTML 코드 삽입
# components.html(html_code, height=600)






# ########################################################################
# ######## streamlit으로 원저작자 파일에서 pydirectinput 기능만 삭제 ########
# ########################################################################
# import streamlit as st
# import streamlit.components.v1 as components

# # 페이지 설정
# st.set_page_config(page_title="Safe Streamlit App", layout="wide")
# st.title("Safe Streamlit 앱")
# st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# # HTML 및 JavaScript 코드 (index.html 내용 수정)
# html_code = """
# <html>
#   <head>
#     <meta charset="UTF-8">
#     <style>
#       body { font-family: Arial, sans-serif; }
#       #action-output { font-size: 24px; font-weight: bold; color: blue; margin-top: 10px; }
#     </style>
#   </head>
#   <body>
#     <div>Custom control based on Teachable Machine</div>
#     <input type="text" id="tm_model_key" value="wef1yJup2">
#     <button type="button" onclick="init()">Load Model</button>
#     <div><canvas id="canvas"></canvas></div>
#     <div id="label-container"></div>
#     <!-- 추가: 인식된 동작 결과 표시 영역 -->
#     <div id="action-output">인식된 동작: None</div>
#     <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
#     <script type="text/javascript">
#       // 전역 변수 선언
#       let model, webcam, ctx, labelContainer, maxPredictions;

#       // 모델 및 웹캠 초기화 함수
#       async function init() {
#           let tm_model_key = document.getElementById("tm_model_key").value;
#           let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
#           let modelURL = URL + "model.json";
#           let metadataURL = URL + "metadata.json";

#           // 모델 및 메타데이터 로드
#           model = await tmPose.load(modelURL, metadataURL);
#           maxPredictions = model.getTotalClasses();

#           // 웹캠 설정
#           const size = 200;
#           const flip = true; // 좌우 반전 여부
#           webcam = new tmPose.Webcam(size, size, flip);
#           await webcam.setup();
#           await webcam.play();
#           window.requestAnimationFrame(loop);

#           // canvas 및 라벨 컨테이너 초기화
#           const canvas = document.getElementById("canvas");
#           canvas.width = size;
#           canvas.height = size;
#           ctx = canvas.getContext("2d");
#           labelContainer = document.getElementById("label-container");
#           for (let i = 0; i < maxPredictions; i++) {
#               labelContainer.appendChild(document.createElement("div"));
#           }
#       }

#       // 반복 함수: 웹캠 프레임 업데이트 및 예측 수행
#       async function loop(timestamp) {
#           webcam.update();
#           await predict();
#           window.requestAnimationFrame(loop);
#       }

#       var prev_action_time = new Date().getTime();
#       var cur_action_time = new Date().getTime();

#       // 예측 함수
#       async function predict() {
#           // 포즈 예측
#           const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
#           // 클래스 예측 (각 클래스의 확률)
#           const prediction = await model.predict(posenetOutput);

#           let action_index = -1;
#           let action_prop = -1;
#           // 예측된 클래스 중 확률이 가장 높은 인덱스 선택
#           for (let i = 0; i < maxPredictions; i++) {
#               const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
#               if (prediction[i].probability > action_prop) {
#                   action_prop = prediction[i].probability;
#                   action_index = i;
#               }
#               labelContainer.childNodes[i].innerHTML = classPrediction;
#           }

#           cur_action_time = new Date().getTime();
#           let diff_time = cur_action_time - prev_action_time;
#           if (diff_time > 200) {
#               prev_action_time = cur_action_time;
#               sendAction(action_index);
#           }
#           drawPose(pose);
#       }

#       // sendAction 함수: 인식된 action_index에 따라 동작 이름을 출력함
#       function sendAction(action_index) {
#           let actionName = "";
#           // 아래 매핑은 Teachable Machine 모델 예측 순서에 맞게 수정 필요
#           if (action_index === 0) {
#               actionName = "Up (위)";
#           } else if (action_index === 1) {
#               actionName = "Down (아래)";
#           } else if (action_index === 2) {
#               actionName = "Right (오른쪽)";
#           } else if (action_index === 3) {
#               actionName = "Left (왼쪽)";
#           } else {
#               actionName = "Unknown Action";
#           }
#           document.getElementById("action-output").innerHTML = "인식된 동작: " + actionName;
#           console.log("Detected action index:", action_index, actionName);
#       }

#       // 포즈 그리기 함수
#       function drawPose(pose) {
#           if (webcam.canvas) {
#               ctx.drawImage(webcam.canvas, 0, 0);
#               if (pose) 
#                   const minPartConfidence = 0.5;
#                   tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
#                   tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
#               }
#           }
#       }
#     </script>
#   </body>
# </html>
# """


# ########################################################################
# ######## pydirectinput없이 브라우저 내 
# # javascript의 KeyboardEvent를 활용하여 
# # 티처블머신에서 인식된 동장에 따라 
# # 키보드 이벤트를 시뮬레이션하는 streamlit 앱 ########
# ########################################################################

# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(page_title="Safe Streamlit App", layout="wide")
# st.title("Safe Streamlit 앱")
# st.write("Teachable Machine 모델을 활용하여 인식된 동작에 따라 브라우저 내 키보드 이벤트를 시뮬레이션합니다.")

# html_code = """
# <html>
#   <head>
#     <meta charset="UTF-8">
#     <style>
#       body { font-family: Arial, sans-serif; }
#       #action-output { font-size: 24px; font-weight: bold; color: blue; margin-top: 10px; }
#     </style>
#   </head>
#   <body>
#     <div>Custom control based on Teachable Machine</div>
#     <input type="text" id="tm_model_key" value="wef1yJup2">
#     <button type="button" onclick="init()">Load Model</button>
#     <div><canvas id="canvas"></canvas></div>
#     <div id="label-container"></div>
#     <!-- 인식된 동작 결과 출력 영역 -->
#     <div id="action-output">인식된 동작: None</div>
#     <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
#     <script type="text/javascript">
#       let model, webcam, ctx, labelContainer, maxPredictions;
      
#       // Teachable Machine 및 웹캠 초기화 함수
#       async function init() {
#           let tm_model_key = document.getElementById("tm_model_key").value;
#           let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
#           let modelURL = URL + "model.json";
#           let metadataURL = URL + "metadata.json";
#           model = await tmPose.load(modelURL, metadataURL);
#           maxPredictions = model.getTotalClasses();
#           const size = 200;
#           const flip = true;
#           webcam = new tmPose.Webcam(size, size, flip);
#           await webcam.setup();
#           await webcam.play();
#           window.requestAnimationFrame(loop);
#           const canvas = document.getElementById("canvas");
#           canvas.width = size;
#           canvas.height = size;
#           ctx = canvas.getContext("2d");
#           labelContainer = document.getElementById("label-container");
#           for (let i = 0; i < maxPredictions; i++) {
#               labelContainer.appendChild(document.createElement("div"));
#           }
#       }
      
#       // 반복 함수
#       async function loop(timestamp) {
#           webcam.update();
#           await predict();
#           window.requestAnimationFrame(loop);
#       }
      
#       var prev_action_time = new Date().getTime();
#       var cur_action_time = new Date().getTime();
      
#       // 예측 함수: Teachable Machine 모델을 이용하여 포즈 예측 후, 가장 높은 확률의 동작 선택
#       async function predict() {
#           const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
#           const prediction = await model.predict(posenetOutput);
#           let action_index = -1;
#           let action_prop = -1;
#           for (let i = 0; i < maxPredictions; i++) {
#               const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
#               if (prediction[i].probability > action_prop) {
#                   action_prop = prediction[i].probability;
#                   action_index = i;
#               }
#               labelContainer.childNodes[i].innerHTML = classPrediction;
#           }
#           cur_action_time = new Date().getTime();
#           let diff_time = cur_action_time - prev_action_time;
#           if (diff_time > 200) {
#               prev_action_time = cur_action_time;
#               sendAction(action_index);
#           }
#           drawPose(pose);
#       }
      
#       // 인식된 동작 인덱스에 따라 키보드 이벤트를 시뮬레이션
#       function sendAction(action_index) {
#           let actionName = "";
#           let keyToSimulate = "";
#           // Teachable Machine 모델의 예측 인덱스에 따른 매핑 (필요 시 수정)
#           if (action_index === 0) {
#               actionName = "Up (위)";
#               keyToSimulate = "ArrowUp";
#           } else if (action_index === 1) {
#               actionName = "Down (아래)";
#               keyToSimulate = "ArrowDown";
#           } else if (action_index === 2) {
#               actionName = "Right (오른쪽)";
#               keyToSimulate = "ArrowRight";
#           } else if (action_index === 3) {
#               actionName = "Left (왼쪽)";
#               keyToSimulate = "ArrowLeft";
#           } else {
#               actionName = "Unknown Action";
#           }
#           document.getElementById("action-output").innerHTML = "인식된 동작: " + actionName;
#           console.log("Detected action index:", action_index, actionName);
#           simulateKeyPress(keyToSimulate);
#       }
      
#       // 지정한 키로 keydown 이벤트를 생성하여 dispatch
#       function simulateKeyPress(key) {
#           if (!key) return;
#           const event = new KeyboardEvent('keydown', {
#               key: key,
#               code: key,
#               bubbles: true,
#               cancelable: true
#           });
#           document.dispatchEvent(event);
#           console.log("Simulated keydown for:", key);
#       }
      
#       // 포즈 그리기 함수
#       function drawPose(pose) {
#           if (webcam.canvas) {
#               ctx.drawImage(webcam.canvas, 0, 0);
#               if (pose) {
#                   const minPartConfidence = 0.5;
#                   tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
#                   tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
#               }
#           }
#       }
#     </script>
#   </body>
# </html>
# """

# components.html(html_code, height=750)

# #ngrok 토큰
# #ngrok config add-authtoken VUPAB2UZQZDFBPGBNEQ55ZJVW6CB3EQG







# ########################################################################
# ######## streamlit으로 원저작자 파일에서 pydirectinput 기능만 삭제 ########
# ########################################################################
# import streamlit as st
# import streamlit.components.v1 as components

# # 페이지 설정
# st.set_page_config(page_title="Safe Streamlit App", layout="wide")
# st.title("Safe Streamlit 앱")
# st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# # HTML 및 JavaScript 코드 (index.html 내용 수정)
# html_code = """
# <html>
#   <head>
#     <meta charset="UTF-8">
#     <style>
#       body { font-family: Arial, sans-serif; }
#       #action-output { font-size: 24px; font-weight: bold; color: blue; margin-top: 10px; }
#     </style>
#   </head>
#   <body>
#     <div>Custom control based on Teachable Machine</div>
#     <input type="text" id="tm_model_key" value="wef1yJup2">
#     <button type="button" onclick="init()">Load Model</button>
#     <div><canvas id="canvas"></canvas></div>
#     <div id="label-container"></div>
#     <!-- 추가: 인식된 동작 결과 표시 영역 -->
#     <div id="action-output">인식된 동작: None</div>
#     <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
#     <script type="text/javascript">
#       // 전역 변수 선언
#       let model, webcam, ctx, labelContainer, maxPredictions;

#       // 모델 및 웹캠 초기화 함수
#       async function init() {
#           let tm_model_key = document.getElementById("tm_model_key").value;
#           let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
#           let modelURL = URL + "model.json";
#           let metadataURL = URL + "metadata.json";

#           // 모델 및 메타데이터 로드
#           model = await tmPose.load(modelURL, metadataURL);
#           maxPredictions = model.getTotalClasses();

#           // 웹캠 설정
#           const size = 200;
#           const flip = true; // 좌우 반전 여부
#           webcam = new tmPose.Webcam(size, size, flip);
#           await webcam.setup();
#           await webcam.play();
#           window.requestAnimationFrame(loop);

#           // canvas 및 라벨 컨테이너 초기화
#           const canvas = document.getElementById("canvas");
#           canvas.width = size;
#           canvas.height = size;
#           ctx = canvas.getContext("2d");
#           labelContainer = document.getElementById("label-container");
#           for (let i = 0; i < maxPredictions; i++) {
#               labelContainer.appendChild(document.createElement("div"));
#           }
#       }

#       // 반복 함수: 웹캠 프레임 업데이트 및 예측 수행
#       async function loop(timestamp) {
#           webcam.update();
#           await predict();
#           window.requestAnimationFrame(loop);
#       }

#       var prev_action_time = new Date().getTime();
#       var cur_action_time = new Date().getTime();

#       // 예측 함수
#       async function predict() {
#           // 포즈 예측
#           const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
#           // 클래스 예측 (각 클래스의 확률)
#           const prediction = await model.predict(posenetOutput);

#           let action_index = -1;
#           let action_prop = -1;
#           // 예측된 클래스 중 확률이 가장 높은 인덱스 선택
#           for (let i = 0; i < maxPredictions; i++) {
#               const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
#               if (prediction[i].probability > action_prop) {
#                   action_prop = prediction[i].probability;
#                   action_index = i;
#               }
#               labelContainer.childNodes[i].innerHTML = classPrediction;
#           }

#           cur_action_time = new Date().getTime();
#           let diff_time = cur_action_time - prev_action_time;
#           if (diff_time > 200) {
#               prev_action_time = cur_action_time;
#               sendAction(action_index);
#           }
#           drawPose(pose);
#       }

#       // sendAction 함수: 인식된 action_index에 따라 동작 이름을 출력함
#       function sendAction(action_index) {
#           let actionName = "";
#           // 아래 매핑은 Teachable Machine 모델 예측 순서에 맞게 수정 필요
#           if (action_index === 0) {
#               actionName = "Up (위)";
#           } else if (action_index === 1) {
#               actionName = "Down (아래)";
#           } else if (action_index === 2) {
#               actionName = "Right (오른쪽)";
#           } else if (action_index === 3) {
#               actionName = "Left (왼쪽)";
#           } else {
#               actionName = "Unknown Action";
#           }
#           document.getElementById("action-output").innerHTML = "인식된 동작: " + actionName;
#           console.log("Detected action index:", action_index, actionName);
#       }

#       // 포즈 그리기 함수
#       function drawPose(pose) {
#           if (webcam.canvas) {
#               ctx.drawImage(webcam.canvas, 0, 0);
#               if (pose) {
#                   const minPartConfidence = 0.5;
#                   tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
#                   tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
#               }
#           }
#       }
#     </script>
#   </body>
# </html>
# """

# # Streamlit에 HTML 삽입
# components.html(html_code, height=750)



