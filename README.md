# 🌍 COVID-19 Global Trend Analysis & Forecasting

A Data Analytics and Machine Learning project that analyzes COVID-19 case trends across multiple countries, performs exploratory data analysis (EDA), forecasts future cases using Facebook Prophet, and provides an interactive Streamlit dashboard for visualization.

---

## 📌 Project Overview

This project demonstrates how data analytics and forecasting techniques can be used to understand the spread of COVID-19. It includes:

- Synthetic COVID-19 dataset generation
- Exploratory Data Analysis (EDA)
- Interactive visualizations using Plotly
- Time series forecasting with Prophet
- Streamlit dashboard for data exploration

---

## 🚀 Features

- 📊 Generate COVID-19 dataset
- 📈 Analyze trends across multiple countries
- 🔍 Interactive line chart visualizations
- 🤖 Forecast future COVID-19 cases
- 🌐 Streamlit web dashboard
- 📁 Well-structured project architecture

---

## 🛠️ Tech Stack

**Programming Language**
- Python

**Libraries**
- Pandas
- NumPy
- Plotly
- Prophet
- Streamlit
- Matplotlib

---

## 📂 Project Structure

```
covid-trend-analysis/
│
├── analysis/
│   └── eda.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── generate_data.py
│   └── covid_data.csv
│
├── docker/
│   └── Dockerfile
│
├── model/
│   ├── forecast.py
│   └── forecast.csv
│
├── reports/
│   └── summary.md
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/covid-trend-analysis.git
```

Move into the project folder

```bash
cd covid-trend-analysis
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Generate Dataset

```bash
python data/generate_data.py
```

### Step 2: Perform Exploratory Data Analysis

```bash
python analysis/eda.py
```

### Step 3: Train Forecast Model

```bash
python model/forecast.py
```

### Step 4: Launch Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Dashboard Features

- Country Selection
- COVID-19 Case Trends
- Interactive Line Charts
- Data Visualization
- Forecast Results

---

## 📈 Forecasting

The project uses **Facebook Prophet**, a time-series forecasting library, to predict future COVID-19 cases.

Model Workflow:

- Load dataset
- Filter country data
- Train Prophet model
- Generate future dates
- Predict future cases
- Export forecast results

---

## 📋 Sample Dataset

| Column | Description |
|---------|-------------|
| date | Date of observation |
| country | Country name |
| cases | Number of reported cases |

---

## 📌 Key Insights

- COVID-19 trends vary across countries.
- Interactive visualization helps identify patterns.
- Prophet predicts future case trends using historical data.
- Dashboard allows easy exploration of country-wise statistics.

---

## 📦 Requirements

- Python 3.9+
- Pandas
- NumPy
- Plotly
- Prophet
- Streamlit
- Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- Real-time COVID-19 data integration
- Death and recovery forecasting
- Vaccination analysis
- Geographic heatmaps
- Model performance evaluation
- Multi-model forecasting comparison

---

## 👨‍💻 Authors

**KAOUS KHAN S AND SUJITHA A**

Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer

---

## 📜 License

This project is intended for educational and learning purposes.

## Steps

1. Install dependencies:
pip install -r requirements.txt

2. Generate dataset:
python data/generate_data.py

3. Run EDA:
python analysis/eda.py

4. Run forecasting:
python model/forecast.py

5. Run dashboard:
streamlit run dashboard/app.py
