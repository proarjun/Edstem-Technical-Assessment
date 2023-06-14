from django.shortcuts import render
from rest_framework import generics
from .models import Contacts
from .serializers import ContactSerializer

# Create your views here.

class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()

class ContactView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()