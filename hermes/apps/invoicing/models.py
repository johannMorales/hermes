from django.db import models
from django.db.models import PROTECT, CASCADE

from hermes.apps.crm.models import Contact
from hermes.apps.store.models import Product, MeasureUnit, PaymentCondition


class Invoice(models.Model):
    series = models.CharField(max_length=4)
    number = models.IntegerField()
    client = models.ForeignKey(Contact, on_delete=PROTECT)
    date = models.DateField()
    payment_condition = models.ForeignKey(PaymentCondition, on_delete=PROTECT)

    class Meta:
        db_table = 'invoice'


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=PROTECT)
    description = models.TextField()
    quantity = models.DecimalField(decimal_places=3, max_digits=10)
    unit = models.ForeignKey(MeasureUnit, on_delete=PROTECT)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'invoice_item'
