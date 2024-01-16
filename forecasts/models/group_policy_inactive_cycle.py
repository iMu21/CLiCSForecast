from django.db import models
from forecasts.models.inactive_cycle import InactiveCycle

class GroupPolicyInactiveCycle(InactiveCycle):
    group_policy_id = models.IntegerField()

    def __str__(self):
        return self.group_policy_id + " - " + self.start_date + " - " + self.end_date