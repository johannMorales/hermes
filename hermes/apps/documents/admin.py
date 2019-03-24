from django.contrib import admin
from .models import DocumentCounter


class DocumentCounterAdmin(admin.ModelAdmin):
    list_display = ['type', 'series', 'number']
    ordering = ['id']


admin.site.register(DocumentCounter, DocumentCounterAdmin)
