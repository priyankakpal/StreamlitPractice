import streamlit as st
import yfinance as yf  
import datetime

st.title("Stock price analysis")

symbol = st.text_input("Enter the ticker", "AAPL")

ticker_data = yf.Ticker(symbol)

col1, col2 = st.columns(2)

with col1:
    startDate = st.date_input("Start Date", datetime.date(2023, 10, 1))

with col2:
    enddate = st.date_input("End date", datetime.date(2024, 10, 1))

ticker_df = ticker_data.history(period='1d',start=startDate, end=enddate)

st.write("We are using raw data of yahoo finance")
st.dataframe(ticker_df.head())

st.write("Price movement chart")
st.line_chart(ticker_df['Close'])