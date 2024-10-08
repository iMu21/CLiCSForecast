import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

def correlations():
    with open('forecasts/data_analysises/correlation.pkl', 'rb') as correlations_file:
        correlation_dict = pickle.load(correlations_file)
        return correlation_dict
    
def getNextMonthInfo():
    file_path = "forecasts/data_analysis_reports/Next_Month_Info.xlsx"
    data = pd.read_excel(file_path)
    data_dict = data.to_dict(orient='records')
    return data_dict[0]
 
def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)
    took_month = 25
 
    last_payments = list(data['Payment Amount'])[-took_month:]
    last_months = list(data['Month'])[-took_month:]
    last_years = list(data['Year'])[-took_month:]
    is_predicted_list = [False] * (took_month)
 
    res = []
    for i in range(len(last_payments)):
        res.append({
            "payment": last_payments[i],
            "month": last_months[i],
            "year": last_years[i],
            "is_predicted": is_predicted_list[i]
        })
    corr = correlations()
    nextMonthInfo = getNextMonthInfo()
    return {"claim_data":res, "correlations":corr, "next_month_info":nextMonthInfo, "cols":get_cols()}

def get_data_frame(data):
    cols = get_cols()

    cleaned_data = {k: v for k, v in data.items() if k in cols}
    df = pd.DataFrame([cleaned_data])
    
    return df

def predict_monthly_payment_amount_with_data(data):
    try:
        df = get_data_frame(data)
        print("Came1")
        with open('forecasts/data_analysises/linear_model.pkl', 'rb') as model_file:
            clf = pickle.load(model_file)
    
        with open('forecasts/data_analysises/scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
            
        scaled = scaler.transform(df)
        predictions = clf.predict(scaled)
        return int(predictions[0][0])
    except Exception as error:
        print(error)

def get_cols():
    return [
        'InsuredCount', 'ChildLessThan18', 'AdultLessThan40', 'MiddleLessThan55', 
        'OldGreaterThan55', 'ActiveWeight_P1', 'ActiveWeight_P3', 'ActiveWeight_P4', 
        'ActiveWeight_P5', 'ActiveWeight_P6', 'ActiveWeight_P7', 'ActiveWeight_P8', 
        'ActiveWeight_P10', 'ActiveWeight_P11', 'ActiveWeight_P12', 
        'ActiveWeight_P13', 'ActiveWeight_P14', 'ActiveWeight_P15', 'ActiveWeight_P16', 
        'ActiveWeight_P17', 'ActiveWeight_P18', 'ActiveWeight_P19', 'ActiveWeight_P21',
        'Male','Others' ,'Female','Married', 'Unmarried', 'Acute', 'Chronic'
    ]
