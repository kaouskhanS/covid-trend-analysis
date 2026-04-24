import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/covid_data.csv")

st.title("COVID-19 Global Trend Dashboard")

country = st.selectbox("Select Country", df["country"].unique())

filtered = df[df["country"] == country]

fig = px.line(filtered, x="date", y="cases", title="Cases Over Time")
st.plotly_chart(fig)
