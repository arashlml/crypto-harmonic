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
horizon = st.number_input(label="Horizon",value=100,min_value=100,max_value=10000,step=1,width=870)
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
with col1:
    symbol=st.selectbox(label="Select symbol",options=symbol_options)

with col2:
    timeframe=st.selectbox(label="Select timeframe",options=timeframe_options.keys())
    if  st.button("Show the patterns 📈"):
        with st.spinner(f"Loading the patterns for {horizon} candles..."):
            fig = find_harmonic_patterns(symbol, timeframe_options[timeframe], horizon)
            st.plotly_chart(fig, use_container_width=True)

intervals = timeframe_options[timeframe]
with col1:
    if st.button("Run backtest 📉"):
        with st.spinner(f'Calculating the performance for {horizon} candles...'):
            fig2,positions = find_positions(symbol, intervals, horizon)
            df_signals = collect_signals(positions)
            y = BinanceCandleData()
            y.get_candles(symbol, y.MIN_5, horizon)
            df_prices = y.df
            df_results = evaluate_all(df_prices, df_signals)
            stats = compute_statistics(df_results)
            st.write(f'Win rate: {stats["win_rate"]} ')
            st.write(f'Risk to reward: {stats["risk_to_reward"]}')
            st.write(f"Average return: {stats["avg_return"]}")
            st.write(f"profit factor: {stats['profit_factor']}")
            st.write(f"sharpe ratio: {stats['sharpe_ratio']}")

    if st.button("Show the last position"):
        fig2, positions = find_positions(symbol, intervals, horizon)
        st.plotly_chart(fig2, use_container_width=True)

