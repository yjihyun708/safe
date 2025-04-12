import threading
import time

import pydirectinput  # Windows 환경에서 실제 키 입력 제어
import streamlit as st
import streamlit.components.v1 as components
from flask import Flask, jsonify, make_response, request

#############################################
# 1. Flask 서버 생성 및 pydirectinput 처리 #
#############################################

flask_app = Flask("keyboard_control")

@flask_app.route("/action", methods=["GET"])
def action():
    index = request.args.get("index")
    print("Received action index:", index)
    
    # 인식된 인덱스에 따라 키보드 입력 시뮬레이션 (예시 매핑)
    if index == '0':
        pydirectinput.press('up')
    elif index == '1':
        pydirectinput.press('down')
    elif index == '2':
        pydirectinput.press('right')
    elif index == '3':
        pydirectinput.press('left')
    else:
        print("Unknown action index:", index)
    
    return make_response(jsonify({"status": 200, "action_index": index}), 200)

def run_flask():
    # Flask 서버를 포트 5001에서 실행 (디버그 모드 비활성화)
    flask_app.run(port=5001, threaded=True)

# 백그라운드에서 Flask 서버 실행 (스트림릿 앱과 병행)
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()
time.sleep(1)  # Flask 서버가 실행될 시간 대기

#############################################
# 2. Streamlit 앱 구성 (HTML/JS 통합)       #
#############################################

st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("Teachable Machine 모델을 활용하여 인식된 동작에 따라 키보드를 제어합니다.")

# 아래 HTML 코드는 기존 index.html 내용을 기반으로 하며,
# 인식된 동작에 따라 로컬 Flask 서버 (pydirectinput 처리)로 fetch 요청을 보냅니다.
html_code = """
<html>
  <head>
    <meta charset="UTF-8">
    <style>
      body { font-family: Arial, sans-serif; }
      #action-output { font-size: 24px; font-weight: bold; color: blue; margin-top: 10px; }
    </style>
  </head>
  <body>
    <div>Custom control based on Teachable Machine</div>
    <input type="text" id="tm_model_key" value="wef1yJup2">
    <button type="button" onclick="init()">Load Model</button>
    <div><canvas id="canvas"></canvas></div>
    <div id="label-container"></div>
    <!-- 인식된 동작 결과와 함께, 키보드 입력 제어 요청 결과를 표시 -->
    <div id="action-output">인식된 동작: None</div>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
    <script type="text/javascript">
      let model, webcam, ctx, labelContainer, maxPredictions;
      async function init() {
          let tm_model_key = document.getElementById("tm_model_key").value;
          let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
          let modelURL = URL + "model.json";
          let metadataURL = URL + "metadata.json";
          model = await tmPose.load(modelURL, metadataURL);
          maxPredictions = model.getTotalClasses();
          const size = 200;
          const flip = true;
          webcam = new tmPose.Webcam(size, size, flip);
          await webcam.setup();
          await webcam.play();
          window.requestAnimationFrame(loop);
          const canvas = document.getElementById("canvas");
          canvas.width = size;
          canvas.height = size;
          ctx = canvas.getContext("2d");
          labelContainer = document.getElementById("label-container");
          for (let i = 0; i < maxPredictions; i++) {
              labelContainer.appendChild(document.createElement("div"));
          }
      }
      async function loop(timestamp) {
          webcam.update();
          await predict();
          window.requestAnimationFrame(loop);
      }
      var prev_action_time = new Date().getTime();
      var cur_action_time = new Date().getTime();
      async function predict() {
          const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
          const prediction = await model.predict(posenetOutput);
          let action_index = -1;
          let action_prop = -1;
          for (let i = 0; i < maxPredictions; i++) {
              const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
              if (prediction[i].probability > action_prop) {
                  action_prop = prediction[i].probability;
                  action_index = i;
              }
              labelContainer.childNodes[i].innerHTML = classPrediction;
          }
          cur_action_time = new Date().getTime();
          let diff_time = cur_action_time - prev_action_time;
          if (diff_time > 200) {
              prev_action_time = cur_action_time;
              sendAction(action_index);
          }
          drawPose(pose);
      }
      // sendAction 함수: 인식된 action_index에 따라 키보드 제어 요청을 보냄
      function sendAction(action_index) {
          let actionName = "";
          if (action_index === 0) {
              actionName = "Up (위)";
          } else if (action_index === 1) {
              actionName = "Down (아래)";
          } else if (action_index === 2) {
              actionName = "Right (오른쪽)";
          } else if (action_index === 3) {
              actionName = "Left (왼쪽)";
          } else {
              actionName = "Unknown Action";
          }
          document.getElementById("action-output").innerHTML = "인식된 동작: " + actionName;
          console.log("Detected action index:", action_index, actionName);
          fetch('http://127.0.0.1:5001/action?index=' + action_index)
          .then(response => response.json())
          .then(data => console.log("Flask 응답:", data))
          .catch(error => console.log("Error:", error));
      }
      function drawPose(pose) {
          if (webcam.canvas) {
              ctx.drawImage(webcam.canvas, 0, 0);
              if (pose) {
                  const minPartConfidence = 0.5;
                  tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
                  tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
              }
          }
      }
    </script>
  </body>
</html>
"""

# Streamlit에 HTML/JavaScript 삽입
components.html(html_code, height=750)
