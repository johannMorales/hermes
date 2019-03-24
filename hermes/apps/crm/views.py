from rest_framework import generics

from .models import Contact
from .serializers import ContactSerializer


class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    pagination_class = None
    serializer_class = ContactSerializer

