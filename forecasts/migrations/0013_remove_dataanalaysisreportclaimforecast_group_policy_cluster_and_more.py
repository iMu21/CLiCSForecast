# Generated by Django 5.0.1 on 2024-01-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0012_rename_group_policy_cluster_product_id_grouppolicyclusterproductinactivecycle_parent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataanalaysisreportclaimforecast',
            name='group_policy_cluster',
        ),
        migrations.AddField(
            model_name='dataanalaysisreportclaimforecast',
            name='group_policy_cluster_active_at_least_one_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dataanalaysisreportclaimforecast',
            name='group_policy_cluster_active_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dataanalaysisreportclaimforecast',
            name='group_policy_cluster_inactive_weight',
            field=models.IntegerField(default=0),
        ),
    ]