import pandas as pd
import pickle

def predict_monthly_payment_amount():
    file_path = "forecasts/data_analysis_reports/Sample_Data.xlsx"
    data = pd.read_excel(file_path)

    predict_no_of_month = 5
    took_month = predict_no_of_month * 5

    # Extracting relevant columns for predictions
    last_payments = list(data['Payment Amount'])[-took_month:-predict_no_of_month]
    last_months = list(data['Month'])[-took_month:]
    last_years = list(data['Year'])[-took_month:]
    is_predicted_list = [False] * (took_month - predict_no_of_month)

    # Drop columns that are not needed
    data = data.drop(columns=["Year", "Month", "Payment Amount"])

    # Load the trained model
    with open('forecasts/data_analysises/linear_model.pkl', 'rb') as file:
        clf = pickle.load(file)
        months_data = data[-predict_no_of_month:]
        predictions = clf.predict(months_data.to_numpy())

        for i in range(predict_no_of_month):
            last_payments.append(int((predictions[i][0]*2)/100000))
            is_predicted_list.append(True)

    # Prepare the results
    res = []
    for i in range(len(last_payments)):
        res.append({
            "payment": last_payments[i],
            "month": last_months[i],
            "year": last_years[i],
            "is_predicted": is_predicted_list[i]
        })

    return res
