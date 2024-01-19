from datetime import timedelta
from django.utils import timezone
from django.db import models
from dateutil.relativedelta import relativedelta
from forecasts.models.base_model import BaseModel
from forecasts.models.group_policy_inactive_cycle import GroupPolicyInactiveCycle

class GroupPolicy(BaseModel):
    group_number = models.CharField(max_length=100)
    premium_payment_type = models.CharField(max_length=100)
    group_policy_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.group_number}'
    
    @classmethod
    def get_active_count_for_date_range(self,start_date, end_date):
        active_dict = []

        current_start_date = start_date.replace(day=1)
        current_end_date = (start_date + relativedelta(months=1)) - timedelta(days=1)

        one_month = timedelta(days=31)

        all_group_policies = GroupPolicy.objects.all()
        inactive_cycles = GroupPolicyInactiveCycle.objects.all()

        while current_end_date <= end_date:
            ids=[]
            for group_policy in all_group_policies:
                if group_policy.effective_date<=current_end_date and not self.is_date_within_inactive_cycle(
                                                                                inactive_cycles,
                                                                                group_policy,
                                                                                current_start_date,
                                                                                current_end_date):
                    ids.append(group_policy.clics_db_id)
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
                                      group_policy, check_start_date,
                                      check_current_end_date):
        return any(
            cycle.group_policy_id == group_policy.clics_db_id and(
                (cycle.start_date <= check_current_end_date and cycle.end_date is None) or
                cycle.start_date <= check_start_date and check_current_end_date <= cycle.end_date
            ) for cycle in inactive_cycles
        )
