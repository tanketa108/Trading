
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

option = st.sidebar.selectbox("Choose", ("Portfolio", "Market Information"))

if option == "Portfolio":
     st.subheader(option)


if option== "Market Information":
     st.subheader(option)
     title = st.text_input('Movie title', 'Life of Brian')
     simbol = "APP"
     st.image(f"http://finviz.com/chart.ashx?t={simbol}")




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

    
     df = pd.DataFrame({
        
          })

     
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




     


