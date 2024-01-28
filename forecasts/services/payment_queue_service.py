from datetime import timedelta
from dateutil.relativedelta import relativedelta
from forecasts.constants import Constants
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.payment_queue import PaymentQueue

def update_payment_statistic():
        print("Payment statistics process start")
        current_start_date = Constants.REPORT_START_DATE.replace(day=1)
        current_end_date = (Constants.REPORT_START_DATE + relativedelta(months=1)) - timedelta(days=1)

        one_month = timedelta(days=31)
        payments = PaymentQueue.objects.all()

        while current_end_date <= Constants.REPORT_END_DATE:
            amount = 0
            for payment in payments:
                if current_start_date<=payment.claim_date<=current_end_date:
                    amount = amount + payment.claim_amount
            year = current_start_date.year
            month = current_start_date.month

            reports = DataAnalaysisReportClaimForecast.objects.filter(year=year,month=month)
            report = None
            if len(reports) > 0:
                report = reports[0]
            else:
                report = DataAnalaysisReportClaimForecast()
                report.year = year
                report.month = month
            report.claim_amount = amount
            current_start_date = (current_start_date+one_month).replace(day=1)
            current_end_date = (current_start_date + relativedelta(months=1)) - timedelta(days=1)
        print("Payment statistics process end")
