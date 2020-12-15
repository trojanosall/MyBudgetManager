from django.db import models
from django.utils import timezone
from money import Money


class Costs(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    registrationDate = models.DateTimeField(
        db_column='registrationDate', blank=True, null=True, verbose_name="Registration Date")
    dateOfPayment = models.DateTimeField(
        db_column='dateOfPayment', blank=True, null=True, verbose_name="Date Of Payment")
    amount = models.IntegerField(
        db_column='amount', blank=True, null=True, verbose_name="Amount")
    description = models.TextField(db_column='description', blank=True, null=True,
                                   verbose_name="Description", help_text="")
    category = models.CharField(db_column='category', max_length=35, blank=True, null=True,
                                verbose_name="Category")

    class Meta:
        managed = False
        db_table = 'costs'
