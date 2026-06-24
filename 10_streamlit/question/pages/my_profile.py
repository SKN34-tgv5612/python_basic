import streamlit as st
st.title("프로필 페이지")
col1 , col2 = st.columns(2)
with col1:
    st.image(
        "https://png.pngtree.com/thumb_back/fh260/background/20250506/pngtree-peaceful-green-field-horizon-desktop-background-image_17251865.jpg"
        , width=300)
with col2:
    st.write("""
             이름 : 윤성호\n
             학과 : 컴퓨터공학부\n
             관심분야 : 개인 비서형 AI 에이전트\n
             취미 : 웹툰/웹소설 읽기\n
             """)

st.divider()

col1 , col2 = st.columns(2)
with col1:
    st.write("지금 기분의 이미지를 표현한다면")
with col2:
    st.image(
        "10_streamlit/question/pages/image.png"
        ,width=300
        )

