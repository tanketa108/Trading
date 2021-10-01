
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
# Welcome to Streamlit!

"""
streamlit.area_chart(data=None, width=0, height=0, use_container_width=True)
>>> chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'])
 st.area_chart(chart_data)
