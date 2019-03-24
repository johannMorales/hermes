from django.db import models


class MeasureUnit(models.Model):
    name = models.CharField(max_length=255)
    display_singular = models.CharField(max_length=255)
    display_plural = models.CharField(max_length=255)
    allows_decimal = models.BooleanField()

    class Meta:
        db_table = 'measure_unit'


class PaymentCondition(models.Model):
    name = models.CharField(max_length=255)
    days_offset = models.IntegerField()

    class Meta:
        db_table = 'payment_condition'


class Product(models.Model):
    name = models.TextField(max_length=255)

    class Meta:
        db_table = 'product'

