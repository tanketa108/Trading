
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

option = st.selectbox(
     '',
     ('Portfolio', 'Market information', 'Portfolio creator'))
st.write('You selected:', option)

if st.selectbox('Portfolio'):
     ## Portfolio
     
     ##
if st.selectbox('Market information'):

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


chart_data = pd.DataFrame()

st.line_chart(chart_data)






