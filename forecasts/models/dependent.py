from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.dependent_inactive_cycle import DependentInactiveCycle
from datetime import timedelta
from dateutil.relativedelta import relativedelta
class Dependent(BaseModel):
    enroll_id = models.IntegerField(default=0)
    gender = models.CharField(max_length=1,default='O')
    birth_date = models.DateField(null=True,blank=True)
    effective_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.clics_db_id} - {self.enroll_id}"
    
    @classmethod
    def get_active_count_for_date_range(self,start_date, end_date):
        active_dict = []

        current_start_date = start_date.replace(day=1)
        current_end_date = (start_date + relativedelta(months=1)) - timedelta(days=1)

        one_month = timedelta(days=31)

        all_obj = Dependent.objects.all()
        inactive_cycles = DependentInactiveCycle.objects.all()

        while current_end_date <= end_date:
            ids=[]
            for obj in all_obj:
                if obj.effective_date<=current_end_date and not self.is_date_within_inactive_cycle(
                                                                                inactive_cycles,
                                                                                obj.clics_db_id,
                                                                                current_start_date,
                                                                                current_end_date):
                    ids.append(obj.clics_db_id)

            active_dict.append({
                'year': current_start_date.year,
                'month': current_start_date.month,
                'ids': ids
            })

            current_start_date = (current_start_date+one_month).replace(day=1)
            current_end_date = (current_start_date + relativedelta(months=1)) - timedelta(days=1)

        return active_dict

    @classmethod
    def is_date_within_inactive_cycle(self,inactive_cycles,
                                      parent_id, check_start_date,
                                      check_current_end_date):
        return any(
            cycle.dependent_id == parent_id and(
                (cycle.start_date <= check_current_end_date and cycle.end_date is None) or
                cycle.start_date <= check_start_date and check_current_end_date <= cycle.end_date
            ) for cycle in inactive_cycles
        )  
