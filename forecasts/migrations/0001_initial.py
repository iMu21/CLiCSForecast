# Generated by Django 5.0.1 on 2024-01-18 19:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(null=True)),
                ('group_policy_cluster_id', models.IntegerField(null=True)),
                ('enroll_id', models.IntegerField(null=True)),
                ('dependent_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('enroll_id', models.IntegerField(default=0)),
                ('gender', models.CharField(default='O', max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DependentInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('dependent_id', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DependentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('dependent_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('group_policy_cluster_product_id', models.IntegerField(default=0)),
                ('coverage_amount', models.DecimalField(decimal_places=3, max_digits=30)),
                ('effective_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DependentProductInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('dependent_product_id', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('group_policy_id', models.IntegerField()),
                ('certificate_number', models.CharField(max_length=100)),
                ('gender', models.CharField(default='o', max_length=1)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('effective_date', models.DateField(default=django.utils.timezone.now)),
                ('group_policy_cluster_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnrollInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('enroll_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnrollProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('enroll_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('group_policy_cluster_product_id', models.IntegerField(default=0)),
                ('coverage_amount', models.DecimalField(decimal_places=3, max_digits=30)),
                ('effective_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnrollProductInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('enroll_product_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('group_number', models.CharField(max_length=100)),
                ('premium_payment_type', models.CharField(max_length=100)),
                ('group_policy_type', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('group_type', models.CharField(max_length=100)),
                ('effective_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyCluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('group_policy_id', models.IntegerField(null=True)),
                ('effective_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyClusterInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group_policy_cluster_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyClusterProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('group_policy_cluster_id', models.IntegerField(default=0)),
                ('group_policy_product_id', models.IntegerField(default=0)),
                ('effective_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyClusterProductInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group_policy_cluster_product_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group_policy_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('group_policy_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('effective_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPolicyProductInactiveCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group_policy_product_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField(default=0)),
                ('claim_entry_id', models.IntegerField(default=0)),
                ('claim_amount', models.DecimalField(decimal_places=3, max_digits=30)),
                ('payable_amount', models.DecimalField(decimal_places=3, max_digits=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clics_db_id', models.IntegerField()),
                ('code', models.CharField(max_length=50)),
                ('claim_type', models.CharField(max_length=50)),
                ('maximum_age', models.IntegerField(null=True)),
                ('product_category', models.CharField(max_length=50)),
                ('lob', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]