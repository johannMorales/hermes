from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import services


@api_view()
def generate_cotizacion(request):
    services.generate_cotizacion()
    return Response({"message": "Cotizacion creada"})


@api_view()
def generate_factura(request):
    services.generate_factura()
    return Response({"message": "Factura creada"})


@api_view()
def generate_boleta(request):
    services.generate_boleta()
    return Response({"message": "Boleta creada"})

