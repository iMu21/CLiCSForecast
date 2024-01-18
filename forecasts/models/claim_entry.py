from django.db import models
from forecasts.models.base_model import BaseModel

class ClaimEntry(BaseModel):
    product_id = models.IntegerField(null=True)
    group_policy_cluster_id = models.IntegerField(null=True)
    enroll_id = models.IntegerField(null=True)
    dependent_id = models.IntegerField(null=True)

    def __str__(self):
        return self.clics_db_id
    
#clics_db_id,product_id,group_policy_cluster_id,enroll_id,dependent_id 
    