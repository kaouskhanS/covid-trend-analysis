import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/covid_data.csv")
df['date'] = pd.to_datetime(df['date'])

fig = px.line(df, x="date", y="cases", color="country", title="COVID Trends")
fig.show()
