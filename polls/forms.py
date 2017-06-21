# -*- encoding: utf-8 -*-
#Biblioteca para trabalhar com formularios - Permite exibir formulario no template, validar
#os dados que foram enviados, exibir erros de validaçao no template, converter os dados enviados
#para tipos em python

# fields: classe responsavel por realizar a validacao
# widgets: representacao do field em HTML

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuario'}), label = '',max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),label = '', max_length=30)

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'lastName', 'cpf', 'email', 'phone', 'city', 'estado', 'bairro', 'street', 'login',
                  'password']

        widgets = {'cpf': TextInput(attrs={'pattern': '^(\d{11})$', 'title': 'Cpf válido com apenas os digitos'}),
                   'email': EmailInput(),
                   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'}),
                   'login': TextInput(attrs={'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'autocomplete': 'new-password'})
                   }


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['firstName', 'fantasyName', 'email', 'phone', 'login',
                  'password']

        widgets = {'email': EmailInput(),
                   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'}),
                   'login': TextInput(attrs={'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'autocomplete': 'new-password'})
                   }

class ConvenioBuscarForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['firstName', 'fantasyName']


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['firstName', 'cpf', 'crm', 'especialidade', 'email', 'phone', 'city', 'address', 'street', 'login', 'password']
        widgets = {'cpf': TextInput(attrs={'pattern': '^(\d{11})$', 'title': '99999999999'}),
                   'crm': TextInput(attrs={'pattern': '^(\d{10})$', 'title': '9999999999'}),
                   'email': EmailInput(),
                   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
                   'login': TextInput(attrs={'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'autocomplete': 'new-password'})
                   }

class MedicoBuscarForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['firstName', 'especialidade']


class HospForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['nome', 'cnpj', 'email', 'phone', 'estado', 'city', 'bairro', 'street', 'login',
                  'password']
        widgets = {'cnpj': TextInput(attrs={'pattern': '^\d{14}$', 'title': '14 digitos de um CNPJ valido'}),
                   'email': EmailInput(),
                   'phone': TextInput(attrs={'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
                   'login': TextInput(attrs={'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'autocomplete': 'new-password'})
                   }


class ModeloExameForm(ModelForm):
    class Meta:
        model = ModeloExame
        fields = ['nome','hospital']


class ExameBuscarForm(ModelForm):
    class Meta:
        model = Exame
        fields = ['nome','hospital']

class ExameMarcar(ModelForm):
    class Meta:
        model = Exame
        fields = ['paciente', 'nome', 'hospital', 'horario' ]

class GerenciarExameForm(ModelForm):
    class Meta:
        model = GerenciarExame
        fields = ['hospital']


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'horario']
        widgets = {'paciente': Select(choices=Patient.objects.all(), attrs={'class': 'form'}),
                   'medico': Select(choices=Medico.objects.all(), attrs={'class': 'form'}),
                   'horario': TextInput(attrs={'placeholder': 'Horario', 'class': 'form', 'type':'datetime'})
                   }

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['paciente', 'horario', 'diagnostico']
        widgets = {'paciente': Select(choices=Patient.objects.all(), attrs={'class': 'form'}),
                   'horario': TextInput(attrs={'placeholder': 'Horario', 'class': 'form', 'type':'datetime'})
                   }


