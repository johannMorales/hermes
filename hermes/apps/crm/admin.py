from django.contrib import admin
from .models import IdentityDocument, PersonaNatural, PersonaJuridica, Contact, Representante


class IdentityDocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol']
    ordering = ['id']


class PersonaNaturalAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'document', 'mobile', 'email', 'phone']
    ordering = ['id']


class PersonaJuridicaAdmin(admin.ModelAdmin):
    list_display = ['name', 'ruc', 'address', 'web']
    ordering = ['id']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['type', 'juridica', 'natural']
    ordering = ['id']


class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ['contact', 'person', 'email', 'mobile', 'phone']
    ordering = ['id']


admin.site.register(IdentityDocument, IdentityDocumentAdmin)
admin.site.register(PersonaNatural, PersonaNaturalAdmin)
admin.site.register(PersonaJuridica, PersonaJuridicaAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Representante, RepresentanteAdmin)
