#app.py
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Set laman utama menjadi full wide
st.set_page_config(layout="wide")

@st.cache_data()
def load_data():
    data = pd.read_csv('./Superstore.csv', parse_dates=['Order Date'])
    return data

data = load_data()

shouldDisplayPivoted = st.checkbox("Pivot data on Order ID")

gb = GridOptionsBuilder()

# makes columns resizable, sortable and filterable by default
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=False,
)

#configures state column to have a 80px initial width
gb.configure_column(field="Order ID", header_name="Order ID", width=120, pivot=True)

#applies a value formatter to Reference Date Column to display as a short date format.
gb.configure_column(
    field="Order Date",
    header_name="Order Date",
    width=110,
    valueFormatter="value != undefined ? new Date(value).toLocaleString('en-US', {dateStyle:'medium'}): ''",
)

gb.configure_column(field="State", header_name="State", width=100)

gb.configure_column(
    field="Customer Name", header_name="Customer Name", width=180, tooltipField="Customer Name"
)

# gb.configure_column(
#     field="Product Name", header_name="Product Name", width=250, tooltipField="Product Name"
# )

#Numeric Columns are right aligned
gb.configure_column(
    field="Quantity",
    header_name="Qty",
    width=65,
    type=["numericColumn"],
    aggFunc="sum"
)

#The last column is the value column and will be formatted using javascript number.toLocaleString()
gb.configure_column(
    field="Profit",
    header_name="Profit",
    width=110,
    type=["numericColumn"],
    valueFormatter="value.toLocaleString()",
    aggFunc="sum"
)

#makes tooltip appear instantly
gb.configure_grid_options(
    tooltipShowDelay=0,
    pivotMode=shouldDisplayPivoted,
    pivotPanelShow="always",
)
go = gb.build()

AgGrid(data, gridOptions=go, height=500, width='100%')