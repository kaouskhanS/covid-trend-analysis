import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2020-01-01", periods=500)
countries = ["USA", "India", "Brazil", "UK", "Germany"]

data = []

for country in countries:
    cases = np.abs(np.random.normal(loc=1000, scale=300, size=len(dates))).astype(int)
    for i in range(len(dates)):
        data.append([dates[i], country, cases[i]])

df = pd.DataFrame(data, columns=["date", "country", "cases"])

df.to_csv("covid_data.csv", index=False)
