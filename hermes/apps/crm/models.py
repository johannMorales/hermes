from django.db import models


class IdentityDocument(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'identity_document'


class PersonaNatural(models.Model):
    identity_document = models.ForeignKey(IdentityDocument, on_delete=models.PROTECT)
    identity_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    mobile = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def document(self):
        return f'{self.identity_document.symbol} {self.identity_number}'

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'persona_natural'


class PersonaJuridica(models.Model):
    name = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    web = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'persona_juridica'


class Contact(models.Model):
    TYPE_JURIDICA = 'TYPE_JURIDICA'
    TYPE_NATURAL = 'TYPE_NATURAL'

    TYPES = (
        (TYPE_JURIDICA, 'Persona Juridica'),
        (TYPE_NATURAL, 'Persona Natural')
    )

    juridica = models.ForeignKey(PersonaJuridica, on_delete=models.CASCADE, null=True, blank=True)
    natural = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPES)

    @property
    def name(self):
        if self.type == self.TYPE_JURIDICA:
            return f'{self.juridica}'
        else:
            return f'{self.natural}'


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'contact'


class Representante(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    mobile = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)

    class Meta:
        db_table = 'representante'

