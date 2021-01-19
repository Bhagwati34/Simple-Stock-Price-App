import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
   # Simple Stock Price App
   Shown are the stock Opening, closing price and volume of companies
   
""")


tickerSymbol = st.text_input('Enter company name in tickerSymbol ')
tickerData = yf.Ticker(tickerSymbol)
startDate = st.date_input('Enter startDate')
endDate = st.date_input('Enter endDate ')
tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)
st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.bar_chart(tickerDf.Volume)
