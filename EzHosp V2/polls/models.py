from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from EzHosp2 import settings


class Paciente(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=11)
	city = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	bairro = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	cpf = models.CharField(max_length=11)
	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class Convenio(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fantasyName = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	def __str__(self):
		return "%s" % (self.user.first_name)


class Medico(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cpf = models.CharField(max_length=11)
	crm = models.CharField(max_length=10)
	especialidade = models.CharField(max_length=50)
	nota = models.IntegerField()
	phone = models.CharField(max_length=11)
	hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
	def __str__(self):
		return "%s - %s" % (self.user.first_name, self.especialidade)


class Hospital(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cnpj = models.CharField(max_length=14)
	phone = models.CharField(max_length=11)
	estado = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	bairro = models.CharField(max_length=30)
	street = models.CharField(max_length=20)
	convenios = models.ManyToManyField(Convenio)
	def __str__(self):
		return "%s" % (self.user.first_name)

class ModeloExame(models.Model):
	nome = models.CharField(max_length=50)
	hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
	def __str__(self):
		return "%s - Hosp: %s" % (self.nome, self.hospital)

class Exame(models.Model):
	nome = models.ForeignKey('ModeloExame', on_delete=models.CASCADE)
	horario = models.DateTimeField()
	paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
	def __str__(self):
		return "%s - Paciente: %s" % (self.nome, self.paciente)

class Consulta(models.Model):
	paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
	medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
	horario = models.DateTimeField()

class Diagnostico(models.Model):
	paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
	medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
	horario = models.DateTimeField()
	diagnostico = models.CharField(max_length=100)