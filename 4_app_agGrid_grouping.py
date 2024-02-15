#app.py
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import datetime

# Set laman utama menjadi full wide
st.set_page_config(layout="wide")

@st.cache_data()
def load_data():
    data = pd.read_csv('./Superstore.csv', parse_dates=['Order Date'])
    return data

data = load_data()

gb = GridOptionsBuilder()

# makes columns resizable, sortable and filterable by default
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=False,
)

# Misalkan Anda memiliki DataFrame 'data' dan ingin mengganti nama kolom 'Order Date' dengan alias 'orderDateAlias'
data.rename(columns={'Order Date': 'orderDateAlias'}, inplace=True)

gb.configure_column(
    field="virtualYear",
    header_name="Order Year",
    valueGetter="new Date(data.orderDateAlias).getFullYear()",
    type=["numericColumn"],
    width=110,
    rowGroup=True,
    hide=True,
)

gb.configure_column(
    field="virtualMonth",
    header_name="Order Month",
    valueGetter="new Date(data.orderDateAlias).toLocaleDateString('id-ID',options={year:'numeric', month:'2-digit'})",
    width=120,
    rowGroup=True,
    hide=True,
)

gb.configure_column(field="State", header_name="State", width=100, 
    rowGroup=True,
    hide=True,
)

gb.configure_column(field="Order ID", header_name="Order ID", 
    width=120, 
    rowGroup=True,
    hide=True,
)

gb.configure_column(
    field="orderDateAlias",
    header_name="Order Date",
    width=110,
    valueFormatter="value != undefined ? new Date(value).toLocaleString('id-ID', {dateStyle:'medium'}): ''",
)

gb.configure_column(
    field="Customer Name", header_name="Customer Name", width=180, 
    tooltipField="Customer Name", 
    rowGroup=True,
)

gb.configure_column(
    field="Segment", header_name="Segment", width=110, tooltipField="Segment"
)

gb.configure_column(
    field="City", header_name="City", width=130, tooltipField="City"
)

gb.configure_column(
    field="Region", header_name="Region", width=90, tooltipField="Region"
)

gb.configure_column(
    field="Category", header_name="Category", width=120, tooltipField="Category"
)

gb.configure_column(
    field="Sub-Category", header_name="Sub-Category", width=130, tooltipField="Sub-Category"
)

gb.configure_column(
    field="Product Name", header_name="Product Name", width=250, tooltipField="Product Name"
)

gb.configure_column(
    field="Quantity",
    header_name="Qty",
    width=65,
    type=["numericColumn"],
)

gb.configure_column(
    field="Profit",
    header_name="Profit",
    width=110,
    type=["numericColumn"],
    valueFormatter="value.toLocaleString()",
)

gb.configure_grid_options(
    autoGroupColumnDef=dict(
        minWidth=300, 
        pinned="left", 
        cellRendererParams=dict(suppressCount=True)
    ),
    domLayout="autoHeight",
    autoSize=True
)

go = gb.build()

AgGrid(data, gridOptions=go, width='100%')