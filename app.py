import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("Teachable Machine 모델을 활용하여 인식된 동작에 따라 브라우저 내 키보드 이벤트를 시뮬레이션합니다.")

# HTML 및 JavaScript 코드 (index.html 기반)
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
    <!-- 추가: 인식된 동작 결과와 키 이벤트 시뮬레이션 결과 표시 영역 -->
    <div id="action-output">인식된 동작: None</div>
    
    <!-- TensorFlow.js 및 Teachable Machine Pose 라이브러리 -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
    
    <script type="text/javascript">
      let model, webcam, ctx, labelContainer, maxPredictions;
      
      // Teachable Machine 및 웹캠 초기화 함수
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
      
      // 반복 함수: 웹캠 프레임 업데이트 후 예측 수행
      async function loop(timestamp) {
          webcam.update();
          await predict();
          window.requestAnimationFrame(loop);
      }
      
      var prev_action_time = new Date().getTime();
      var cur_action_time = new Date().getTime();
      
      // 예측 함수: Teachable Machine 모델을 이용해 포즈 예측 후, 가장 높은 확률의 동작 선택
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
          let diff_time = cur_action_time -_
