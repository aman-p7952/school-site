from django.db import models

# Create your models here.

class Fee(models.Model):
    student_id = models.CharField(max_length=10)
    fee_paid_months = models.IntegerField(default=0)

class FeeStructure(models.Model):
    student_class = models.IntegerField()
    fee_name = models.CharField(max_length=30)
    fee_value = models.FloatField()
    