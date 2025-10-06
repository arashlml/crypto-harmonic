from FindingPatterns import find_harmonic_patterns
from FindingPositions import find_positions
from harmonic_backtester import (
    collect_signals,
    evaluate_all,
    compute_statistics,
)
from pyharmonics.marketdata import BinanceCandleData
import streamlit as st
import pandas as pd

st.set_page_config(page_title="My App", page_icon="💸", layout="wide")


st.title("Harmonic patterns performance on cryptos 🪙")
col1 , col2 = st.columns(2)
df=pd.read_csv("symbols.csv")
symbol_options=df.values
timeframe_options={
        "1 minutes": '1m',
        "5 minutes": '5m',
        "15 minutes" : '15m',
        "30 minutes" : '30m',
        "1 hour" : '1h',
        "4 hour": '4h',
        "1 day" : '1d',
        "1 week": '1w',
        "1 month": '1M'
    }

horizon = 10000
with col1:
    symbol=st.selectbox("Select symbol",symbol_options)

with col2:
    timeframe=st.selectbox("Select timeframe",timeframe_options.keys())
    if st.button("Show the patterns 📈"):
        with st.spinner("Loading the patterns..."):
            fig = find_harmonic_patterns(symbol, timeframe_options[timeframe], horizon)
            st.plotly_chart(fig, use_container_width=True)

intervals = timeframe_options[timeframe]
with col1:
    if st.button("Run backtest 📉"):
        with st.spinner('Calculating the performance for 10000 candles...'):
            positions = find_positions(symbol, intervals, horizon)
            df_signals = collect_signals(positions)
            y = BinanceCandleData()
            y.get_candles(symbol, y.MIN_5, horizon)
            df_prices = y.df
            df_results = evaluate_all(df_prices, df_signals)
            stats = compute_statistics(df_results)
            st.write(f'Win rate: {stats["win_rate"]} ')
            st.write(f"Average return: {stats["avg_return"]}")
            st.write(f"profit factor: {stats['profit_factor']}")
            st.write(f"sharpe ratio: {stats['sharpe_ratio']}")





