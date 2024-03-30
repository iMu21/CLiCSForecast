import pickle
import pandas as pd

def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)
    last_payments = list(data['Payment Amount'])[-6:-2]
    last_months = list(data['Month'])[-6:-1]
    last_years = list(data['Year'])[-6:-1]
    data = data.drop(columns=['ActiveWeight_P20', 'ActiveWeight_P2','ActiveWeight_P9','ActiveWeight_P14',"Year","Month",'Payment Amount'])
    test=data.iloc[[-1]]
    
    with open('forecasts/data_analysises/multioutput_gb_model.pkl','rb') as file:
        clf = pickle.load(file)
        prediction = clf.predict(test)
    last_payments.append(prediction[0][0])
    res=[]
    for i in range(5):
        res.append({"payment":last_payments[i],"month":last_months[i],"year":last_years[i]})

    return res