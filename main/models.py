from django.db import models


class Employee(models.Model):
    employee = models.CharField(max_length=100, blank=True)
    personnel_number = models.CharField(max_length=100)
    guid_employee = models.CharField(unique=True, max_length=100)
    guid_individual = models.CharField(max_length=100)
    sid = models.CharField(max_length=100, primary_key=True)
    archive = models.CharField(max_length=100, blank=True)
    contract_type = models.CharField(max_length=100, blank=True)
    employment_type = models.CharField(max_length=100, blank=True)
    condition = models.CharField(max_length=100, blank=True)
    status_date = models.DateField()
    subdivision = models.CharField(max_length=100, blank=True)
    guid_subdivision = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    guid_position = models.CharField(max_length=100, blank=True)
    employment_date = models.DateField()
    personnel_movement_date = models.DateField('%d/%m/%Y')
    dismissal_date = models.DateField()
    settlement_type = models.CharField(max_length=100, blank=True)
    salary_chts = models.DecimalField(
        null=True, max_digits=8, decimal_places=2, blank=True)
    email = models.EmailField(unique=True, max_length=40, blank=True)
    login = models.CharField(max_length=100)
    head_of_division = models.CharField(max_length=100, blank=True)
    guid_head_of_division = models.CharField(max_length=100, blank=True)
    head_of_higher_division = models.CharField(max_length=100, blank=True)
    guid_head_of_higher_division = models.CharField(max_length=100, blank=True)
    guid_calendar = models.CharField(
        max_length=100, blank=True)
    cnt_positions = models.DecimalField(
        null=True, max_digits=4, decimal_places=2, blank=True)
    bss_sid = models.CharField(max_length=100, blank=True)  # там конечно куча цифр но разделены дефисами
    for_date = models.DateField()
    actual = models.CharField(max_length=100, blank=True)
    change_column = models.CharField(max_length=100, blank=True)
    docid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.employee

    # class Meta:
    #  db_table = "ertelecom"
    # db_table = "ER_TELECOM_TEST_BASE"
