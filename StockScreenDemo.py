
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
# Welcome to Streamlit!

"""
"""
# add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Portfolio", "Information", "News")

if add_selectbox == "Portfolio":
	st.subheader("Portfolio")

else
"""




