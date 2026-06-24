import streamlit as st
st.title("사용자 입력 받는 페이지")

col1 , col2 = st.columns(2)

with col1:
    nickname = st.text_input("닉네임 입력")
    age = st.number_input("나이 입력",max_value=100, min_value=13)
    nation = st.selectbox("국가 선택", ("한국","미국","중국","일본","외계"))
    habbit = st.radio("취미 선택",("맛집 탐방","영화 감상","음악 감상","뜨게질"))
    # 개인정보동의 여부
    is_agree = st.checkbox("개인정보 제공 동의")
with col2:
    if is_agree:
        st.write(f"""
        이름이 뭐야? {nickname}

        몇 살이야? {age}

        어디서 왔어? {nation}

        취미가 뭐야? {habbit}

        개인정보 제공에 동의해? {is_agree}
        """)
        st.write("당신은 {}입니다.".format(nation))
