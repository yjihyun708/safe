

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