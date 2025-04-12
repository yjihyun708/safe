import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("Teachable Machine 모델을 활용하여 인식된 동작에 따라 브라우저 내 키보드 이벤트를 시뮬레이션합니다.")

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
    <!-- 인식된 동작 결과 출력 영역 -->
    <div id="action-output">인식된 동작: None</div>
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
      
      // 반복 함수
      async function loop(timestamp) {
          webcam.update
