from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Patient(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    cellPhone = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
