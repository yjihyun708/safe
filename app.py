###################################################################################
# pyngrok (Python NGrok 라이브러리)**를 활용하여 local Streamlit 앱을 외부에 노출하는 코드
# Teachable Machine을 이용한 커스텀 컨트롤 HTML을 포함하며, 원본에서 물리 키보드 제어를 위한 pydirectinput 기능은 제거됨
###################################################################################

############ ngrok 설치 ############
# 1. choco install ngrok
# 2. ngrok config add-authtoken 2vcnEs3bMVWxJNVSF0piz2I83zR_6DeaHhtgg2VDG2U5BCEWx
# 3. 임시 도메인 ngrok http http://localhost:8080

############ 코드 설명 ############
# 1. pyngrok 터널 생성
# 코드 시작부분에서 pyngrok을 사용해 Streamlit 기본 포트(8501)를 외부에 노출하는 터널을 생성합니다.

# 2. Streamlit 앱 설정
# Streamlit 페이지 설정 및 기본 타이틀, 설명을 작성합니다.

# 3. HTML/JavaScript 삽입
# 원본 HTML 코드를 수정하여 pydirectinput 관련 코드는 제거한 후, Teachable Machine 모델을 사용해 웹캠과 예측 결과를 출력하는 기능을 포함합니다.

# 4. 스트림릿 컴포넌트
# streamlit.components.v1의 components.html 함수를 사용하여 HTML 코드를 앱에 삽입합니다.
###################################################################################

# 1. 필수 라이브러리 설치
# pip install streamlit pyngrok

# 코드 실행
# streamlit run app.py
###################################################################################

import streamlit as st
import streamlit.components.v1 as components
from pyngrok import ngrok

# ngrok 터널 생성 (Streamlit 기본 포트: 8501)
public_url = ngrok.connect(8501)
st.write("ngrok URL:", public_url)

# 페이지 설정
st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# HTML 코드: pydirectinput 기능 제거 후 Teachable Machine 컨트롤 코드 사용
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
    <!-- 추가: 인식된 동작 결과 표시 영역 -->
    <div id="action-output">인식된 동작: None</div>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
    <script type="text/javascript">
      let model, webcam, ctx, labelContainer, maxPredictions;

      // 모델 및 웹캠 초기화 함수
      async function init() {
          let tm_model_key = document.getElementById("tm_model_key").value;
          let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
          let modelURL = URL + "model.json";
          let metadataURL = URL + "metadata.json";

          // 모델과 메타데이터 로드
          model = await tmPose.load(modelURL, metadataURL);
          maxPredictions = model.getTotalClasses();

          // 웹캠 설정
          const size = 200;
          const flip = true; // 좌우 반전 여부
          webcam = new tmPose.Webcam(size, size, flip);
          await webcam.setup();
          await webcam.play();
          window.requestAnimationFrame(loop);

          // canvas 및 라벨 컨테이너 초기화
          const canvas = document.getElementById("canvas");
          canvas.width = size;
          canvas.height = size;
          ctx = canvas.getContext("2d");
          labelContainer = document.getElementById("label-container");
          for (let i = 0; i < maxPredictions; i++) {
              labelContainer.appendChild(document.createElement("div"));
          }
      }

      // 반복 함수: 웹캠 프레임 업데이트 및 예측 수행
      async function loop(timestamp) {
          webcam.update();
          await predict();
          window.requestAnimationFrame(loop);
      }

      var prev_action_time = new Date().getTime();
      var cur_action_time = new Date().getTime();

      // 예측 함수
      async function predict() {
          const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
          const prediction = await model.predict(posenetOutput);

          let action_index = -1;
          let action_prop = -1;
          // 예측된 클래스 중 확률이 가장 높은 인덱스 선택
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

      // 인식된 action_index에 따른 동작 출력
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
      }

      // 포즈 그리기 함수
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

# 스트림릿 컴포넌트를 이용해 HTML 코드 삽입
components.html(html_code, height=600)
