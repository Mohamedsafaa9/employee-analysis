import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Employee Analysis Dashboard")
st.title("Employee Analysis Dashboard")

@st.cache_data
def load_data(path="employees.csv"):
    df = pd.read_csv(path, parse_dates=['HireDate'])
    return df

df = load_data("employees.csv")

st.sidebar.header("Filters")
dept = st.sidebar.multiselect("Department", options=df['Department'].unique(), default=df['Department'].unique())

filtered = df[df['Department'].isin(dept)]

st.metric("Total employees", len(filtered))
st.dataframe(filtered.head(30))

st.header("Employees per Department")
st.bar_chart(filtered['Department'].value_counts())