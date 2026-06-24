import streamlit as st
import pandas as pd

# 가상 데이터 생성
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '점수': [85, 90, 95]
})

# CSV로 변환
csv = df.to_csv().encode('utf-8')

# 다운로드 버튼
st.download_button(label="CSV 다운로드", data=csv, file_name='data.csv', mime='text/csv')