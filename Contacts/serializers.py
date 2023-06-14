from rest_framework.serializers import ModelSerializer
from .models import Contacts

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'