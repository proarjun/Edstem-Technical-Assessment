from django.db import models

from  django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
    full_name = models.CharField(max_length = 50)
    address = models.TextField(max_length=150)
    phone = models.IntegerField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.full_name