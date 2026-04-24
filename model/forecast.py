from prophet import Prophet
import pandas as pd

df = pd.read_csv("../data/covid_data.csv")
df = df[df['country'] == 'India']

df = df.rename(columns={"date": "ds", "cases": "y"})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

forecast[['ds','yhat']].to_csv("forecast.csv", index=False)
