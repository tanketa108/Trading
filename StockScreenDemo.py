
import pandas as pd
import yfinance as yahooFinance
import streamlit as st
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
import numpy as np
import time
import re 

header = st.beta_container()
Portfolio = st.beta_container()
marketinf = st.beta_container()

with header:
     st.title('MY APP')

option = st.sidebar.selectbox("Choose", ("Portfolio", "Market Information"))

if option == "Portfolio":
     st.subheader(option)
     titulos = [1,['Fecha','Saldo broker','Saldo Criptomonedas','Saldo cuenta'],2,['01/01/2020', '1000', '500', '500']]


     
     
     #fig = go.Figure(data=go.Table(header=('Saldo broker','Saldo Criptomonedas','Saldo cuenta')), cells=dict())
     #fig=px.pie(values='values', names='titles')
     
     #fig.update_layout()
     
     #st.write(fig)


if option== "Market Information":
     st.subheader(option)
     st.image(f"https://www.tradingview.com/chart/hxphyLUX/?symbol=SP%3ASPX")
     #tickers = pd.read_html('http://en.wikipedia/wiki/Dow_Jones_Industrial_Average')[1]
     #tickers = tickers.Symbol.to_list()
     
     
     title = st.text_input('APP', 'BAC')
     if title == "APP":
          st.subheader('Hi APP')
          inf = yf.Ticker(title).info
     if title == "BAC":
          st.subheader('Hi BAC')
          inf = yf.Ticker(title).info

simbol = 'APP'
 #st.image(f"http://finviz.com/chart.ashx?t={simbol}")




with Portfolio:
     st.header('Patrimonio')
     #patrimonio = pd.read_csv('https://github.com/tanketa108/Trading/blob/main/data/Patrimonio.csv')
     #st.write('.C:/Python/Trading/data/Patrimonio.csv')
     #df1 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv")
     
     # Add table data
     table_data = [['Fecha','Saldo broker','Criptomonedas','Saldo cuenta'],
              ['01-01-2021', 18, 4, 0],
              ['01-02-2021', 18, 5, 0],
              ['01-03-2021', 16, 5, 0],
              ['01-04-2021', 13, 8, 0],
              ['01-05-2021', 13, 8, 0],
              ['01-06-2021', 12, 5, 0]]

    
     

     


# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 1 second, so the change is clearer.
time.sleep(1)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)




     


