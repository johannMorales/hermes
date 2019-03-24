from rest_framework import serializers

from hermes.apps.store.models import MeasureUnit, PaymentCondition, Product


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ('id', 'name', 'display_singular', 'display_plural', 'allows_decimal')


class PaymentConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCondition
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')
