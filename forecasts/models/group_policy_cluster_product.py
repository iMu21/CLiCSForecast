from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.group_policy_cluster_product_inactive_cycle import GroupPolicyClusterProductInactiveCycle
from datetime import timedelta
from django.db import models

from dateutil.relativedelta import relativedelta
class GroupPolicyClusterProduct(BaseModel):
    group_policy_cluster_id = models.IntegerField(default=0)
    group_policy_product_id = models.IntegerField(default=0)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_cluster_id}'
    
    @classmethod
    def get_active_count_for_date_range(self,start_date, end_date):
        active_dict = []
        current_start_date = start_date.replace(day=1)
        current_end_date = (start_date + relativedelta(months=1)) - timedelta(days=1)
        one_month = timedelta(days=31)

        all_obj = GroupPolicyClusterProduct.objects.all()
        inactive_cycles = GroupPolicyClusterProductInactiveCycle.objects.all()

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
            cycle.group_policy_cluster_product_id == parent_id and(
                (cycle.start_date <= check_current_end_date and cycle.end_date is None) or
                cycle.start_date <= check_start_date and check_current_end_date <= cycle.end_date
            ) for cycle in inactive_cycles
        )

    