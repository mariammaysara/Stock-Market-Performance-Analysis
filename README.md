### 🚗 Tesla Stock Close Price Predictor
Welcome to the Tesla Stock Close Price Predictor! This is an end-to-end machine learning project that forecasts the closing price of Tesla stock using historical data and a user-friendly web interface powered by Streamlit.

### Project Overview

This application takes in various stock market features and predicts the closing price of Tesla (TSLA) shares. The goal is to help investors or enthusiasts estimate the stock price more intelligently using machine learning techniques.

 ### Features

User input for:

Open Price

High Price

Low Price

Volume

Daily % Change

7-Day Moving Average

30-Day Moving Average

High-Low Difference

Real-time prediction of TSLA close price using trained ML models.

Beautiful interactive interface with animations (Lottie).

### Live Demo
👉 Click here to view the app : https://stock-market-performance-analysis-aoe59uj5x2erxy8uaggv8c.streamlit.app/


📁 Project Structure
├── app/
│   └── app.py               # Streamlit application file
├── data/
│   └── raw/tesla_data.csv   # Raw dataset
├── models/
│   └── xgboost_model.pkl    # Trained ML model
├── notebooks/
│   ├── 01_EDA.ipynb         # Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb # Data cleaning and feature engineering
│   └── 03_Modeling.ipynb    # Model training and evaluation
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation (you’re reading it!)

⚙️ How to Run Locally

1- Clone the repository:
git clone https://github.com/mariammaysara/Stock-Market-Performance-Analysis.git
cd Stock-Market-Performance-Analysis
2-Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3- Install the dependencies:
pip install -r requirements.txt
4- Run the app:
streamlit run app/app.py

### Technologies Used

Python 3.12

pandas, numpy, seaborn, matplotlib

scikit-learn, xgboost

yfinance (data fetching)

Streamlit (web app framework)

Lottie animations (UX enhancement)

📸 Screenshot


![Screenshot 2025-04-26 092433](https://github.com/user-attachments/assets/b80787bc-b200-4b3c-8a24-d8fa422fb25d)

🙋‍♀️ Author

Made by Mariam Maysara
This project is licensed under the MIT License - feel free to use it for learning or inspiration


