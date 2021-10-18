
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
     # Initialize a figure with ff.create_table(table_data)
     fig = ff.create_table(table_data, height_constant=60)

     table_data.show
     df = pd.DataFrame({
        
          })

     
     chart_data = pd.DataFrame()
     st.line_chart(chart_data)
     
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




     


