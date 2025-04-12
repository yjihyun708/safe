########################################################################
######## streamlit으로 원저작자 파일에서 pydirectinput 기능만 삭제 ########
########################################################################
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# HTML 및 JavaScript 코드 (index.html 내용 수정)
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
      // 전역 변수 선언
      let model, webcam, ctx, labelContainer, maxPredictions;

      // 모델 및 웹캠 초기화 함수
      async function init() {
          let tm_model_key = document.getElementById("tm_model_key").value;
          let URL = 'https://teachablemachine.withgoogle.com/models/' + tm_model_key + '/';
          let modelURL = URL + "model.json";
          let metadataURL = URL + "metadata.json";

          // 모델 및 메타데이터 로드
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
          // 포즈 예측
          const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
          // 클래스 예측 (각 클래스의 확률)
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

      // sendAction 함수: 인식된 action_index에 따라 동작 이름을 출력함
      function sendAction(action_index) {
          let actionName = "";
          // 아래 매핑은 Teachable Machine 모델 예측 순서에 맞게 수정 필요
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

# Streamlit에 HTML 삽입
components.html(html_code, height=750)



