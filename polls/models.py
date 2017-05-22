from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models


class Patient(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	city = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	bairro = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	cpf = models.CharField(max_length=11)
	#convenio = models.ForeignKey('Convenio', blank = True)


class Convenio(models.Model):
	firstName = models.CharField(max_length=50)
	fantasyName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Medico(models.Model):
	firstName = models.CharField(max_length=50)
	cpf = models.CharField(max_length=11)
	crm = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Hospital(models.Model):
	nome = models.CharField(max_length=50)
	cnpj = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	estado = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	bairro = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	#convenio = models.ManyToManyField(Convenio)
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Exame(models.Model):
	nome = models.CharField(max_length=50)
