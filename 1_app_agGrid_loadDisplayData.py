#app.py
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Set laman utama menjadi full wide
st.set_page_config(layout="wide")

@st.cache_data()
def load_data():
    data = pd.read_csv('./Superstore.csv', parse_dates=['Order Date'])
    return data

data = load_data()

# Format kolom 'Order Date' sesuai dengan kebutuhan
data['Order Date'] = data['Order Date'].dt.strftime('%Y-%m-%d')

AgGrid(data, height=500, width='100%')