from django.db import models
import csv
from forecasts.models.base_model import BaseModel

class DataAnalaysisReportClaimForecast(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)

    group_policy_active_weight = models.IntegerField(default=0)
    group_policy_inactive_weight = models.IntegerField(default=0)
    group_policy_active_at_least_one_day = models.IntegerField(default=0)

    group_policy_cluster_active_weight = models.IntegerField(default=0)
    group_policy_cluster_inactive_weight = models.IntegerField(default=0)
    group_policy_cluster_active_at_least_one_day = models.IntegerField(default=0)

    enroll_active_weight = models.IntegerField(default=0)
    enroll_inactive_weight = models.IntegerField(default=0)
    enroll_active_at_least_one_day = models.IntegerField(default=0)
    enroll_active_old_age_weight = models.IntegerField(default=0)
    enroll_inactive_old_age_weight = models.IntegerField(default=0)
    enroll_active_mid_age_weight = models.IntegerField(default=0)
    enroll_inactive_mid_age_weight = models.IntegerField(default=0)
    enroll_active_young_age_weight = models.IntegerField(default=0)
    enroll_inactive_young_age_weight = models.IntegerField(default=0)
    enroll_active_child_age_weight = models.IntegerField(default=0)
    enroll_inactive_child_age_weight = models.IntegerField(default=0)

    enroll_product_active_weight = models.IntegerField(default=0)
    enroll_product_inactive_weight = models.IntegerField(default=0)
    enroll_product_active_at_least_one_day = models.IntegerField(default=0)
    enroll_product_GM_active_weight = models.IntegerField(default=0)
    enroll_product_GL_active_weight = models.IntegerField(default=0)
    enroll_product_IL_active_weight = models.IntegerField(default=0)
    enroll_product_ID_active_weight = models.IntegerField(default=0)
    enroll_product_BM_active_weight = models.IntegerField(default=0)
    enroll_product_BL_active_weight = models.IntegerField(default=0)
    enroll_product_GM_inactive_weight = models.IntegerField(default=0)
    enroll_product_GL_inactive_weight = models.IntegerField(default=0)
    enroll_product_IL_inactive_weight = models.IntegerField(default=0)
    enroll_product_ID_inactive_weight = models.IntegerField(default=0)
    enroll_product_BM_inactive_weight = models.IntegerField(default=0)
    enroll_product_BL_inactive_weight = models.IntegerField(default=0)

    dependent_active_weight = models.IntegerField(default=0)
    dependent_inactive_weight = models.IntegerField(default=0)
    dependent_active_at_least_one_day = models.IntegerField(default=0)
    dependent_active_old_age_weight = models.IntegerField(default=0)
    dependent_inactive_old_age_weight = models.IntegerField(default=0)
    dependent_active_mid_age_weight = models.IntegerField(default=0)
    dependent_inactive_mid_age_weight = models.IntegerField(default=0)
    dependent_active_young_age_weight = models.IntegerField(default=0)
    dependent_inactive_young_age_weight = models.IntegerField(default=0)
    dependent_active_child_age_weight = models.IntegerField(default=0)
    dependent_inactive_child_age_weight = models.IntegerField(default=0)

    dependent_product_active_weight = models.IntegerField(default=0)
    dependent_product_inactive_weight = models.IntegerField(default=0)
    dependent_product_active_at_least_one_day = models.IntegerField(default=0)
    dependent_product_GM_active_weight = models.IntegerField(default=0)
    dependent_product_GL_active_weight = models.IntegerField(default=0)
    dependent_product_IL_active_weight = models.IntegerField(default=0)
    dependent_product_ID_active_weight = models.IntegerField(default=0)
    dependent_product_BM_active_weight = models.IntegerField(default=0)
    dependent_product_BL_active_weight = models.IntegerField(default=0)
    dependent_product_GM_inactive_weight = models.IntegerField(default=0)
    dependent_product_GL_inactive_weight = models.IntegerField(default=0)
    dependent_product_IL_inactive_weight = models.IntegerField(default=0)
    dependent_product_ID_inactive_weight = models.IntegerField(default=0)
    dependent_product_BM_inactive_weight = models.IntegerField(default=0)
    dependent_product_BL_inactive_weight = models.IntegerField(default=0)
    
    claim_amount = models.IntegerField(default=0)
    
    @classmethod
    def generate_report_csv(self):
        csv_file_path = BaseModel.get_file_path('data_analysis_reports','DataAnalaysisReportClaimForecast.csv')
        field_names = [field.name for field in self._meta.get_fields()]

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(field_names)
            for obj in self.objects.all():
                row_values = [str(getattr(obj, field)) for field in field_names]
                csv_writer.writerow(row_values)