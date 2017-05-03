from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class Patient(models.Model):
	firstName = models.CharField(max_length=50)
	cpf = models.CharField(max_length=11)
	lastName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	cellPhone = models.CharField(max_length=15)
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Convenio(models.Model):
	firstName = models.CharField(max_length=50)
	fantasyName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Medico(models.Model):
	firstName = models.CharField(max_length=50)
	cpf = models.CharField(max_length=11)
	crm = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	cellPhone = models.CharField(max_length=15)
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
