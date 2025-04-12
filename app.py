import streamlit as st

st.title("👋 Streamlit Cloud 데모 앱")

name = st.text_input("이름을 입력하세요:")

if name:
    st.success(f"{name}님, 환영합니다! 😊")
