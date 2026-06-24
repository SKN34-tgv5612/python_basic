import streamlit as st
import pandas as pd

# 데이터 생성
data = pd.DataFrame({
    "제품": ["A", "B", "C"],
    "expenses": [
        [120, 300, 450, 600],   # A 제품 월별 지출
        [200, 500, 700, 900],   # B 제품 월별 지출
        [150, 250, 350, 550],   # C 제품 월별 지출
    ]
})

st.data_editor(
    data,
    column_config={
        "expenses": st.column_config.BarChartColumn(
            "Monthly Expenses",
            y_min=0,
            y_max=1000
        )
    }
)