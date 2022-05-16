# Generated by Django 4.0.1 on 2022-01-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee', models.CharField(blank=True, max_length=200)),
                ('personnel_number', models.CharField(max_length=250)),
                ('guid_employee', models.CharField(max_length=250, unique=True)),
                ('guid_individual', models.CharField(max_length=250)),
                ('sid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('archive', models.CharField(blank=True, max_length=200)),
                ('contract_type', models.CharField(blank=True, max_length=200)),
                ('employment_type', models.CharField(blank=True, max_length=200)),
                ('condition', models.CharField(blank=True, max_length=200)),
                ('status_date', models.DateField()),
                ('subdivision', models.CharField(blank=True, max_length=200)),
                ('guid_subdivision', models.CharField(blank=True, max_length=200)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('guid_position', models.CharField(blank=True, max_length=200)),
                ('employment_date', models.DateField()),
                ('personnel_movement_date', models.DateField()),
                ('dismissal_date', models.DateField()),
                ('settlement_type', models.CharField(blank=True, max_length=200)),
                ('salary_chts', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=40, unique=True)),
                ('login', models.CharField(max_length=200)),
                ('head_of_division', models.CharField(blank=True, max_length=200)),
                ('guid_head_of_division', models.CharField(blank=True, max_length=200)),
                ('head_of_higher_division', models.CharField(blank=True, max_length=200)),
                ('guid_head_of_higher_division', models.CharField(blank=True, max_length=200)),
                ('guid_calendar', models.CharField(blank=True, max_length=200)),
                ('cnt_positions', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('bss_sid', models.CharField(blank=True, max_length=100)),
                ('for_date', models.DateField()),
                ('actual', models.CharField(blank=True, max_length=200)),
                ('change_column', models.CharField(blank=True, max_length=200)),
                ('docid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]