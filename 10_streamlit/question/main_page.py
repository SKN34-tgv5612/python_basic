import streamlit as st

st.title("오늘은 수요일")
st.header("오늘은 Streamlit 배우는 날🔥🔥🔥")
st.subheader("Streamlit으로 나만의 데모 페이지 만들기~~~!")

text = st.text_input("오늘은 내가 만들어고싶은 사이트는?!")
st.write(text)
st.link_button(url=text, label=f"{text}접속하기")
if text:
    st.success(f"{text} 접속 중!!!", icon="✅")