# Generated by Django 5.0.1 on 2024-01-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0008_dataanalaysisreportclaimforecast_group_policy_active_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataanalaysisreportclaimforecast',
            name='group_policy_total_active_at_least_one_day',
            field=models.IntegerField(default=0),
        ),
    ]
