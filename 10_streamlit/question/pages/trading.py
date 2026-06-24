import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import ccxt
chart , sidebar = st.columns(2)
candles = []

close_price = 100
if "timeline" not in st.session_state:
    st.session_state["timeline"] = "15m"

if "stock" not in st.session_state:
    st.session_state["stock"] = "BTC/USDT"

if "logs" not in st.session_state:
    st.session_state["logs"] = []
binance = ccxt.binance()
with chart:
    st.session_state['stock'] = st.selectbox('종목',['BTC/USDT','ETH/USDT'],index=['BTC/USDT','ETH/USDT'].index(st.session_state['stock']))
    st.session_state['timeline'] = st.selectbox(
        '타임라인',
        list(binance.timeframes),
        index=list(binance.timeframes).index(st.session_state['timeline'])
        ) 
    ohlcv = binance.fetch_ohlcv(st.session_state['stock'], st.session_state['timeline'],limit=close_price)
    for row in ohlcv:
        candles.append(
            {
                "time": int(row[0] / 1000),
                "open": row[1],
                "high": row[2],
                "low": row[3],
                "close": row[4],
            }
        )
    series = [
        {
            "type": "Candlestick",
            "data": candles,
        }
        ]

    st.set_page_config(layout="wide")
    renderLightweightCharts(
        [
            {
                "series": series,
            }
        ],
        "main-chart",
        )
with sidebar:
    st.markdown(
        """
        <style>
        .st-key-buy button {
            background-color: #16a34a;
            color: white;
            border: none;
        }

        .st-key-buy button:hover {
            background-color: #15803d;
            color: white;
        }

        .st-key-sell button {
            background-color: #dc2626;
            color: white;
            border: none;
        }

        .st-key-sell button:hover {
            background-color: #b91c1c;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    trade_type = st.selectbox("거래방식 : ",("지정가",'시장가'))
    st.write(f"현제 가격 : {candles[-1]['close']}")
    
    buy =  st.button("매수",key='buy',width="stretch",type='primary')
    sell = st.button("매도",key='sell',width="stretch",type='primary')

    
    if buy:
        st.session_state["logs"].append(f"{trade_type} : {candles[-1]['close']} 에 매수주문이 체결되었습니다.")
    if sell:
        st.session_state["logs"].append(f"{trade_type} : {candles[-1]['close']} 에 매도주문이 체결되었습니다.")

    for log in reversed(st.session_state["logs"]):
        st.success(log, icon="✅")