from rest_framework import generics

from hermes.apps.store.models import MeasureUnit, PaymentCondition, Product
from hermes.apps.store.serializers import MeasureUnitSerializer, PaymentConditionSerializer, ProductSerializer


class MeasureUnitListAPIView(generics.ListAPIView):
    queryset = MeasureUnit.objects.all()
    pagination_class = None
    serializer_class = MeasureUnitSerializer


class PaymentConditionListAPIView(generics.ListAPIView):
    queryset = PaymentCondition.objects.all()
    pagination_class = None
    serializer_class = PaymentConditionSerializer


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    pagination_class = None
    serializer_class = ProductSerializer

