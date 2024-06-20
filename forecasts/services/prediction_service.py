import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
 
def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)
 
    predict_no_of_month = 1
    took_month = 20
 
    last_payments = list(data['Payment Amount'])[-took_month:-predict_no_of_month]
    last_months = list(data['Month'])[-took_month:]
    last_years = list(data['Year'])[-took_month:]
    is_predicted_list = [False] * (took_month - predict_no_of_month)
 
    data = data.drop(columns=['Month', 'Year'])
 
    with open('forecasts/data_analysises/linear_model.pkl', 'rb') as model_file:
        clf = pickle.load(model_file)
   
    with open('forecasts/data_analysises/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
 
    test = data[-predict_no_of_month:]  
    X_last_row = test.drop(columns=["Payment Amount"])
    
    X_last_row_scaled = scaler.transform(X_last_row)

    predictions = clf.predict(X_last_row_scaled)
 
    for i in range(predict_no_of_month):
        last_payments.append(int(predictions[i][0]))
        is_predicted_list.append(True)

    res = []
    for i in range(len(last_payments)):
        res.append({
            "payment": last_payments[i],
            "month": last_months[i],
            "year": last_years[i],
            "is_predicted": is_predicted_list[i]
        })

    return res

def get_data_frame(data):
    cols = [
        'InsuredCount', 'ChildLessThan18', 'AdultLessThan40', 'MiddleLessThan55', 
        'OldGreaterThan55', 'ActiveWeight_P1', 'ActiveWeight_P3', 'ActiveWeight_P4', 
        'ActiveWeight_P5', 'ActiveWeight_P6', 'ActiveWeight_P7', 'ActiveWeight_P8', 
        'ActiveWeight_P9', 'ActiveWeight_P10', 'ActiveWeight_P11', 'ActiveWeight_P12', 
        'ActiveWeight_P13', 'ActiveWeight_P14', 'ActiveWeight_P15', 'ActiveWeight_P16', 
        'ActiveWeight_P17', 'ActiveWeight_P18', 'ActiveWeight_P19', 'ActiveWeight_P21'
    ]

    cleaned_data = {k: v for k, v in data.items() if k in cols}
    df = pd.DataFrame([cleaned_data])
    
    return df

def predict_monthly_payment_amount_with_data(data):
    df = get_data_frame(data)

    with open('forecasts/data_analysises/linear_model.pkl', 'rb') as model_file:
        clf = pickle.load(model_file)
   
    with open('forecasts/data_analysises/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    scaled = scaler.transform(df)

    predictions = clf.predict(scaled)
    
    return int(predictions[0][0])

