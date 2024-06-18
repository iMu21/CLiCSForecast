import pickle
import pandas as pd

def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)
    predict_month=5
    took_month=predict_month*3
    last_payments = list(data['Payment Amount'])[-took_month:-predict_month]
    last_months = list(data['Month'])[-took_month:]
    last_years = list(data['Year'])[-took_month:]
    is_predicted_list = [False]*(took_month-predict_month)
    data = data.drop(columns=["Year","Month",'Payment Amount'])
    
    with open('forecasts/data_analysises/multioutput_gb_model.pkl','rb') as file:
        clf = pickle.load(file)
        
        for i in range(1,predict_month+1):
            month_data=data.iloc[[-i]]
            prediction = clf.predict(month_data)
            last_payments.append(prediction[0][0])
            is_predicted_list.append(True)
    res=[]
    for i in range(len(last_payments)):
        res.append({"payment":last_payments[i],"month":last_months[i],"year":last_years[i],"is_predicted":is_predicted_list[i]})

    return res