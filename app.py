#### Streamlit 앱 내에서 JavaScript를 이용해 키보드 입력 이벤트를 시뮬레이션하는 예제 코드



import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="키보드 이벤트 시뮬레이션", layout="wide")
st.title("Streamlit에서 키보드 이벤트 시뮬레이션")

html_code = """
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>키보드 이벤트 시뮬레이션</title>
    <style>
      body { font-family: Arial, sans-serif; }
      #output { margin-top: 20px; font-weight: bold; color: blue; }
      #inputField { width:300px; height:30px; font-size:16px; }
    </style>
    <script>
      // simulateKeyPress 함수: 입력받은 key 값으로 keydown 이벤트를 생성하여 dispatch 합니다.
      function simulateKeyPress(key) {
        const event = new KeyboardEvent('keydown', {
          key: key,
          code: 'Key' + key.toUpperCase(),
          keyCode: key.toUpperCase().charCodeAt(0),
          which: key.toUpperCase().charCodeAt(0),
          bubbles: true,
          cancelable: true
        });
        document.dispatchEvent(event);
        console.log("Simulated keydown event for key: " + key);
        document.getElementById("output").innerHTML = "Simulated keydown event for key: " + key;
      }

      // 예시로 inputField에 keydown 이벤트 리스너를 추가하여 콘솔에 출력해봅니다.
      window.onload = function() {
        const inputField = document.getElementById('inputField');
        inputField.addEventListener('keydown', function(e) {
          console.log('keydown 이벤트 감지:', e.key);
        });
      }
    </script>
  </head>
  <body>
    <h2>키보드 이벤트 시뮬레이션 예제</h2>
    <input type="text" id="inputField" placeholder="여기에 텍스트 입력">
    <br><br>
    <!-- 버튼 클릭 시 'A'키의 이벤트 시뮬레이션 -->
    <button onclick="simulateKeyPress('a')">키 'A' 입력 이벤트 시뮬레이션</button>
    <div id="output">아직 이벤트 없음</div>
  </body>
</html>
"""

components.html(html_code, height=400)
