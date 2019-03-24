from django.db import models


class DocumentCounter(models.Model):
    TYPE_BOLETA = "BOLETA"
    TYPE_FACTURA = "FACTURA"
    TYPE_COTIZACION = "COTIZACION"

    TYPES = (
        (TYPE_BOLETA, "Boleta"),
        (TYPE_FACTURA, "Factura"),
        (TYPE_COTIZACION, "Cotizacion")
    )

    type = models.CharField(max_length=15, choices=TYPES, blank=False, unique=True)
    series = models.CharField(max_length=10, blank=False)
    number = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'document_counter'
