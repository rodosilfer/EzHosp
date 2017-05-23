from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from .models import *


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'lastName', 'cpf', 'email', 'phone', 'city', 'estado', 'bairro', 'street', 'login',
                  'password']

        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
                   'lastName': TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form'}),
                   'cpf': TextInput(attrs={'placeholder': 'CPF', 'class': 'form', 'pattern': '^(\d{11})$', 'title': '99999999999'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Celular', 'class': 'form', 'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'}),
                   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                   'estado': TextInput(attrs={'placeholder': 'Estado', 'class': 'form'}),
                   'bairro': TextInput(attrs={'placeholder': 'Bairro', 'class': 'form'}),
                   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete': 'new-password'})
                   }


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['firstName', 'fantasyName', 'email', 'phone', 'login',
                  'password']

        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
                   'fantasyName': TextInput(attrs={'placeholder': 'Nome Fantasia', 'class': 'form'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '3199999999'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete': 'new-password'})
                   }


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['firstName', 'cpf', 'crm', 'email', 'phone', 'city', 'address', 'street', 'login', 'password']
        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
                   'cpf': TextInput(attrs={'placeholder': 'CPF', 'class': 'form', 'pattern': '^(\d{11})$', 'title': '99999999999'}),
                   'crm': TextInput(attrs={'placeholder': 'CRD', 'class': 'form', 'pattern': '^(\d{10})$', 'title': '9999999999'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Celular', 'class': 'form', 'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
                   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                   'address': TextInput(attrs={'placeholder': 'Endereço', 'class': 'form'}),
                   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete': 'new-password'})
                   }


class HospForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['nome', 'cnpj', 'email', 'phone', 'estado', 'city', 'bairro', 'street', 'login',
                  'password']
        widgets = {'nome': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
                   'cnpj': TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?(\d{10}(\d{1})?)$', 'title': '031999999999'}),
                   'estado': TextInput(attrs={'placeholder': 'Estado', 'class': 'form'}),
                   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                   'bairro': TextInput(attrs={'placeholder': 'Bairro', 'class': 'form'}),
                   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   #'convenio': Select(choices=Convenio.objects.all(), attrs={'class': 'form'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete': 'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete': 'new-password'})
                   }


class ExameForm(ModelForm):
    class Meta:
        model = Exame
        fields = ['nome']
        widgets = {'nome': TextInput(attrs={'placeholder': 'Nome', 'class': 'form'})
                   }
