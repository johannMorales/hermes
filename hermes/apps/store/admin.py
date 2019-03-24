from django.contrib import admin

from hermes.apps.store.models import MeasureUnit, PaymentCondition, Product


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_singular', 'display_plural', 'allows_decimal']
    ordering = ['id']


class PaymentConditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'days_offset']
    ordering = ['id']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']


admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(PaymentCondition, PaymentConditionAdmin)
admin.site.register(Product, ProductAdmin)
