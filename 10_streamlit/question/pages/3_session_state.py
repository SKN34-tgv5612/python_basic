import streamlit as st

st.title("Counter")
if 'customer_count' not in st.session_state:
    st.session_state['customer_count'] = 0

add_btn = st.button("손님 한 명 추가요~!")
if add_btn:
    st.session_state['customer_count'] += 1

reset_btn = st.button("오늘 장사 끝! 손님 수 초기화할게요~")
if reset_btn:
    st.session_state['customer_count'] = 0

st.write(f"지금까지 온 손님 수: {st.session_state['customer_count']}")