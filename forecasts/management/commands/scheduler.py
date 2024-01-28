from django.core.management.base import BaseCommand
import schedule
import time
import datetime
from forecasts.constants import Constants, ProcessStatus
from forecasts.services.dependent_product_service import update_dependent_product_statistics
from forecasts.services.dependent_service import update_dependent_statistics
from forecasts.services.enroll_product_service import update_enroll_product_statistics

from forecasts.services.enroll_service import update_enroll_statistics
from forecasts.services.group_policy_cluster_service import update_group_policy_cluster_statistics
from forecasts.services.group_policy_service import update_group_policy_statistics
from forecasts.services.payment_queue_service import update_payment_statistic

class Command(BaseCommand):
    help = 'Run scheduled tasks'

    def make_enroll_processing_available():
        if Constants.ENROLL_PROCESS_STATUS == ProcessStatus.SLEEP:
            Constants.ENROLL_PROCESS_STATUS = ProcessStatus.AVAILABLE
            Constants.ENROLL_BATCH_SIZE = 1000
            Constants.ENROLL_MAX_PAGE_SIZE = 412
            Constants.ENROLL_RUNNING_PAGE = 0
            Constants.ENROLL_PROCESS_STATUS = ProcessStatus.AVAILABLE
            print("Enroll statistic processing is available now.")


    def handle(self, *args, **options):
        # Trigger tasks immediately
        update_group_policy_statistics()
        update_group_policy_cluster_statistics()
        update_payment_statistic()
        update_enroll_statistics()
        update_enroll_product_statistics()
        update_dependent_statistics()
        update_dependent_product_statistics()

        #Scheduled tasks
        schedule.every(24).hours.do(self.make_enroll_processing_available)

        schedule.every(24).hours.do(update_group_policy_statistics)
        schedule.every(24).hours.do(update_group_policy_cluster_statistics)
        schedule.every(24).hours.do(update_payment_statistic)

        schedule.every(30).seconds.do(update_enroll_statistics)
        schedule.every(30).seconds.do(update_enroll_product_statistics)
        schedule.every(30).seconds.do(update_dependent_statistics)
        schedule.every(30).seconds.do(update_dependent_product_statistics)

        # Run the scheduler loop
        while True:
            schedule.run_pending()
            time.sleep(1)
 