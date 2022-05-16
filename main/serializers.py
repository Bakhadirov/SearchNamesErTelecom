# from abc import ABC
#
# from django.contrib.auth.models import User
from rest_framework import serializers

#
#
from main.models import Employee


class SerializerSearcherView(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee', 'personnel_number', 'guid_employee', 'guid_individual', 'sid', 'archive', 'contract_type',
                  'employment_type', 'condition', 'status_date', 'subdivision', 'guid_subdivision', 'position',
                  'guid_position',
                  'employment_date', 'personnel_movement_date', 'dismissal_date', 'settlement_type', 'salary_chts',
                  'email', 'login', 'head_of_division', 'guid_head_of_division', 'head_of_higher_division',
                  'guid_head_of_higher_division', 'guid_calendar', 'cnt_positions', 'bss_sid', 'for_date',
                  'actual', 'change_column']
        # db_table = "er_telecom_test_base"
