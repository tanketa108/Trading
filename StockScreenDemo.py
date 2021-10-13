
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
import numpy as np
import time

st.header('MY APP')
st.subheader('This is a subheader')



df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
df
chart_data = pd.DataFrame()
st.line_chart(chart_data)

fig=px.pie(df, values = 'first colum', names = 'second column')
pie_col.write(fig)

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
option = st.selectbox(
     '',
     ('Portfolio', 'Market information', 'Portfolio creator'))
st.write('You selected:', option)

