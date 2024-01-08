import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def predict_next_month_claim_amount():
    import os

    # Get the project's base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the file path
    data_path = os.path.join(BASE_DIR, 'forecasts','csv_training_data', 'claim_records.csv')
    dataframe = pd.read_csv(data_path)
    dataframe = dataframe.dropna()

    # Convert the 'claim_date' column to datetime
    dataframe['claim_date'] = pd.to_datetime(dataframe['claim_date'])

    # Extract year and month from the claim_date
    dataframe['year'] = dataframe['claim_date'].dt.year
    dataframe['month'] = dataframe['claim_date'].dt.month

    # Group by year and month, then sum the claim amount
    monthly_totals = dataframe.groupby(['year', 'month'])['claim_amount'].sum().reset_index()

    X = monthly_totals[['year', 'month']]
    y = monthly_totals['claim_amount']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the next month
    last_month = monthly_totals[['year', 'month']].iloc[-1]
    next_month = [(last_month['month'] % 12) + 1]  # Cycle through months
    next_year = last_month['year'] + (1 if last_month['month'] == 12 else 0)
    prediction = model.predict([[next_year, next_month[0]]])[0]
    
    return prediction

    
