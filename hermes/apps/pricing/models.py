from django.db import models
from django.db.models import PROTECT

from hermes.apps.crm.models import Contact
from hermes.apps.store.models import MeasureUnit, Product, PaymentCondition


class Cotizacion(models.Model):
    client = models.ForeignKey(Contact, on_delete=models.PROTECT)
    includes_igv = models.BooleanField()
    series = models.CharField(max_length=20)
    number = models.IntegerField()
    date = models.DateField()
    payment_condition = models.ForeignKey(PaymentCondition, on_delete=PROTECT, null=True)

    class Meta:
        db_table = 'cotizacion'


class CotizacionItem(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(decimal_places=3, max_digits=10)
    unit = models.ForeignKey(MeasureUnit, on_delete=models.PROTECT)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'cotizacion_item'
