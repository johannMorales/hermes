from django.apps import AppConfig


class DocumentsAppConfig(AppConfig):
    name = 'hermes.apps.documents'
    label = 'documents'
    verbose_name = 'Documents'


default_app_config = 'hermes.apps.documents.DocumentsAppConfig'