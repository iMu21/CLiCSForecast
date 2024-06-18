import pickle
import pandas as pd

def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)
    last_payments = list(data['Payment Amount'])[-6:-1]
    last_months = list(data['Month'])[-6:]
    last_years = list(data['Year'])[-6:]
    data = data.drop(columns=["Year","Month",'Payment Amount'])
    last_month_data=data.iloc[[-1]]
    
    with open('forecasts/data_analysises/multioutput_gb_model.pkl','rb') as file:
        clf = pickle.load(file)
        prediction = clf.predict(last_month_data)
    last_payments.append(prediction[0][0])
    res=[]
    for i in range(len(last_payments)):
        res.append({"payment":last_payments[i],"month":last_months[i],"year":last_years[i]})

    return res