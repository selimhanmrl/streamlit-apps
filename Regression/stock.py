import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import datetime


df = pd.read_csv("bist.csv")



st.write("""
         
        ## Simple Stock Price App
         
         """)

with st.sidebar:
    sound = st.selectbox('Select Stock', df.iloc[:,0])
st.write("""Show are the stock closing price and volume of """ + sound + " !")

         
trickerSymbol = sound + '.IS'
tickerData = yf.Ticker(trickerSymbol)


today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(today.year, 1, 1)
dec_31 = datetime.date(today.year, 1, 1)

#st.write()
with st.sidebar:
    date = st.date_input(
        "Select your vacation for next year",
        (jan_1, datetime.date(today.year, today.month, today.day)),
        format="MM.DD.YYYY",
    )

if len(date) == 1:
    tickerDf = tickerData.history(period='1d', start=date[0])
else:
    if date[0] > date[1]:
        temp = date[0]
        date[0] = date[1]
        date[1] = temp 
    tickerDf = tickerData.history(period='1d', start=date[0], end=date[1])

#st.write(date[0], date[1])



st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

#st.dataframe(df.loc[df['0'] == sound], use_container_width=True)