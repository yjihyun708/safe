########################################################################
######## streamlit으로 원저작자 파일에서 pydirectinput 기능만 삭제 ########
########################################################################
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="Safe Streamlit App", layout="wide")
st.title("Safe Streamlit 앱")
st.write("아래 영역은 Teachable Machine 모델을 활용한 커스텀 컨트롤 입니다.")

# HTML 및 JavaScript 코드 (원래 index.html의 내용)
html_code = """
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <div>Custom control based on Teachable Machine</div>
    <input type="text" id="tm_model_key" value="wef1yJup2">
    <button type="button" onclick="init()">Load Model</button>
    <div><canvas id="canvas"></canvas></div>
    <div id="label-container"></div>
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

      // 반복 함수: 웹캠 프레임 업데이트 및 예측
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
          // 클래스 예측
          const prediction = await model.predict(posenetOutput);

          let action_index = -1;
          let action_prop = -1;
          for (let i = 0; i < maxPredictions; i++) {
              const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
              // 가장 높은 확률의 예측 선택
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

      // 액션 전송 함수 (원래는 서버 API 호출하던 부분을 콘솔 출력으로 대체)
      function sendAction(action_index) {
          console.log("Detected action index:", action_index);
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

# st.components.v1.html를 사용하여 HTML 코드 삽입
components.html(html_code, height=650)




###############################################################
########### pydirectinput 기능 삭제한 streamlit 코드 ###########
###############################################################
# import streamlit as st

# # 페이지 설정 (Page Configuration)
# st.set_page_config(page_title="Safe Streamlit App", layout="wide")

# # 타이틀 및 설명
# st.title("Safe Streamlit 앱")
# st.write("아래 버튼을 클릭해서 방향키 '시뮬레이션' 메시지를 확인합니다. (Click a button to simulate the direction keys.)")

# # 상단에 "위" (Up) 버튼 배치
# if st.button("↑ 위 (Up)"):
#     st.success("위 키가 눌렸습니다! (Up key pressed)")

# # 가운데 행: 왼쪽(Left)과 오른쪽(Right) 버튼 배치
# col_left, col_center, col_right = st.columns([1, 2, 1])
# with col_left:
#     if st.button("← 왼쪽 (Left)"):
#         st.success("왼쪽 키가 눌렸습니다! (Left key pressed)")
# with col_right:
#     if st.button("→ 오른쪽 (Right)"):
#         st.success("오른쪽 키가 눌렸습니다! (Right key pressed)")

# # 하단에 "아래" (Down) 버튼 배치
# if st.button("↓ 아래 (Down)"):
#     st.success("아래 키가 눌렸습니다! (Down key pressed)")



################################################
########### streamlit으로 변경한 코드 ###########
################################################

# import pydirectinput as pag
# import streamlit as st

# # 페이지 설정 (Page Configuration)
# st.set_page_config(page_title="Safe Streamlit App", layout="wide")

# # 타이틀 및 설명
# st.title("Safe Streamlit 앱")
# st.write("아래 버튼을 클릭해서 방향키를 시뮬레이션합니다. (Click a button to simulate the direction keys.)")

# # 상단에 "위" (Up) 버튼 배치
# if st.button("↑ 위 (Up)"):
#     pag.press('up')
#     st.success("위 키가 눌렸습니다! (Up key pressed)")

# # 가운데 행: 왼쪽(Left)과 오른쪽(Right) 버튼 배치
# col_left, col_center, col_right = st.columns([1, 2, 1])
# with col_left:
#     if st.button("← 왼쪽 (Left)"):
#         pag.press('left')
#         st.success("왼쪽 키가 눌렸습니다! (Left key pressed)")
# with col_right:
#     if st.button("→ 오른쪽 (Right)"):
#         pag.press('right')
#         st.success("오른쪽 키가 눌렸습니다! (Right key pressed)")

# # 하단에 "아래" (Down) 버튼 배치
# if st.button("↓ 아래 (Down)"):
#     pag.press('down')
#     st.success("아래 키가 눌렸습니다! (Down key pressed)")

################################################
################# 원저작자 코드 #################
################################################

# import pydirectinput as pag
# from flask import Flask, jsonify, make_response, render_template, request

# # please import pydirectinput instead of pyautogui for windows user
# # import pydirectinput as pag

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def main():
#     return render_template('index.html')

# @app.route("/action", methods=["GET"])
# def action():
#     index = request.args.get('index')
#     print("index : " + index)

#     if index == '1':
#         pag.press('up')
#     elif index == '2':
#         pag.press('down')
#     elif index == '3':
#         pag.press('right')
#     elif index == '4':
#         pag.press('left')
    
#     return make_response(jsonify({"status number": 200}), 200)
  
# if __name__ == "__main__":
#   app.run(port=5001)