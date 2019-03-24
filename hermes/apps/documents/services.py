from .models import DocumentCounter


def generate_document(document_code):
    database_counter = DocumentCounter.objects.get(type=document_code)
    database_counter.number = database_counter.number + 1;
    database_counter.save(force_update=True)


def generate_boleta():
    return generate_document(DocumentCounter.TYPE_BOLETA)


def generate_factura():
    return generate_document(DocumentCounter.TYPE_FACTURA)


def generate_cotizacion():
    return generate_document(DocumentCounter.TYPE_COTIZACION)


