from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import TextInput, ModelForm, EmailInput, PasswordInput, DateTimeInput, Select, fields

from EzHosp2 import settings
from polls.models import *


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')
		widgets = {'first_name': TextInput(attrs={'required':'true'}),
				   'last_name': TextInput(attrs={'required':'true'}),
				   'email': EmailInput(attrs={'required':'true'}),
				   'password': PasswordInput(),
				   }
class UserForm2(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'email', 'username', 'password')
		widgets = {'first_name': TextInput(attrs={'required':'true'}),
				   'email': EmailInput(attrs={'required':'true'}),
				   'password': PasswordInput(),
				   }
class EditUserForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		widgets = {'first_name': TextInput(attrs={'required':'true'}),
				   'last_name': TextInput(attrs={'required':'true'}),
				   'email': EmailInput(attrs={'required':'true'}),
				   }
class EditUserForm2(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'email')
		widgets = {'first_name': TextInput(attrs={'required':'true'}),
				   'email': EmailInput(attrs={'required':'true'}),
				   }
class SearchUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name']

class PacienteForm(ModelForm):
	class Meta:
		model = Paciente
		fields = ['cpf', 'phone', 'city', 'estado', 'bairro', 'street']

		widgets = {'cpf': TextInput(attrs={'pattern': '^(\d{11})$', 'title': 'Cpf válido com apenas os digitos'}),
				   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'}),
				   }

class MedicoForm(ModelForm):
	class Meta:
		model = Medico
		fields = ['cpf', 'crm', 'especialidade', 'hospital', 'phone']
		widgets = {'cpf': TextInput(attrs={'pattern': '^(\d{11})$', 'title': '99999999999'}),
				   'crm': TextInput(attrs={'pattern': '^(\d{10})$', 'title': '9999999999'}),
				   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
				   }

class HospitalForm(ModelForm):
	class Meta:
		model = Hospital
		fields = ['cnpj', 'convenios', 'phone', 'estado', 'city', 'bairro', 'street']
		widgets = {'cnpj': TextInput(attrs={'pattern': '^\d{14}$', 'title': '14 digitos de um CNPJ valido'}),
				   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
				   }

class ConvenioForm(ModelForm):
	class Meta:
		model = Convenio
		fields = ['fantasyName', 'phone']

		widgets = {'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'})}

class ModeloExameForm(ModelForm):
	class Meta:
		model = ModeloExame
		fields = ['nome', ]

class ExameForm(ModelForm):
	class Meta:
		model = Exame
		fields = ['nome', 'horario' ]
		widgets = {'horario': DateTimeInput(format=settings.DATETIME_INPUT_FORMATS, attrs={'pattern': '^\d{2}\/\d{2}\/(\d{2}|\d{4})\s\d{2}:\d{2}$', 'title': 'A data deve estar no formato: MM/DD/YYYY HH:MM'}) }

class BuscaExameForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name',]

class ConsultaForm(ModelForm):
	class Meta:
		model = Consulta
		fields = ['medico', 'horario']
		widgets = { 'horario': DateTimeInput(format=settings.DATETIME_INPUT_FORMATS, attrs={'pattern': '^\d{2}\/\d{2}\/(\d{2}|\d{4})\s\d{2}:\d{2}$', 'title': 'A data deve estar no formato: MM/DD/YYYY HH:MM'}) }

class DiagnosticoForm(ModelForm):
	class Meta:
		model = Diagnostico
		fields = ['paciente', 'diagnostico']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(DiagnosticoForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['paciente'].queryset = Paciente.objects.filter(consulta__medico=user.medico)
