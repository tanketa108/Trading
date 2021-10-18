
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
import re 


header = st.beta_container()
Portfolio = st.beta_container()
marketinf = st.beta_container()

with header:
     st.title('MY APP')



with Portfolio:
     st.header('Patrimonio')
     #patrimonio = pd.read_csv('.C:/Python/Trading/data/Patrimonio.csv')
     #st.write('.C:/Python/Trading/data/Patrimonio.csv')
     
     df = pd.DataFrame({
        
          })
     df
     
     chart_data = pd.DataFrame()
     st.line_chart(chart_data)
     titles = ['Fecha','Saldo broker','Criptomonedas','Saldo cuenta']
     values = [ 900, 950, 750]

with marketinf:
     st.header('Market information')





option = st.selectbox(
     '',
     ('Portfolio', 'Market information', 'Portfolio creator'))
st.title(option)
   
    ## fig = go.Figure()


   #  fig=px.pie(values='values', names='titles')
     
    # fig.update_layout()
     
     # st.write(fig)






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




     


