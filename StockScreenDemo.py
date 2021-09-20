
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

option = st.sidebasr.selectbox("Dashboard", ("Cartera","Stocktwists","Twitter", "Seguimiento"))

st.header(option)

if option == "Cartera":
	st.subheader("Cartera")

##subir archivo file = st.file_uploader("Pick a file')
		df = pd.read_csv("Portfolio")
		st.line_chart(df)
##
if option == "Seguimiento":
	st.subheader("Seguimiento")

	st.write("""
		# Stock Price
		""")

	tickerSymbol = 

	tickerData = yf.Ticker(tickerSymbol) 
	# get the historical prices for the ticker
	tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2021-07-21')

	st.line_chart(tickerDf.Close)
	st.line_chart(tickerDf.Volume)



if option == "Stocktwists":
	st.subheader("Stocktwists")

if option == "Twitter":
	st.subheader("Twitter")

    
 
