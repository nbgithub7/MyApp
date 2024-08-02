import requests
import streamlit as st
from datetime import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


#Header
st.header("Trading Dashboard")

#Accept the stock name and make an object for yfinance
stockName = st.text_input("Enter Stock name",'')
st.write("stock: " + stockName)

stockName_yf = ''
if stockName:
    stockName_yf = yf.Ticker(str(stockName))
    #stockName_yf.info

#Download information, includes Adjusted Closed Price
if stockName_yf:
    #st.write("here")
    stock_download = yf.download(str(stockName), period="max", interval="1mo")
    #stock_download
    #st.write("there")

    stock_adjClose = stock_download[["Adj Close"]]
    stock_adjClose.rename(columns={"Adj Close": "price_t"}, inplace=True)
    
    stock_adjClose["returns"] = stock_adjClose["price_t"].pct_change()
    stock_adjClose["returns %"] = stock_adjClose["returns"] * 100

    stock_adjClose



    


