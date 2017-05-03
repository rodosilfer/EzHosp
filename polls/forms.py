from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'cpf', 'lastName', 'email', 'phone', 'cellPhone', 'city', 'address', 'street', 'login',
                  'password']

        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
		   'cpf': TextInput(attrs={'placeholder': 'CPF', 'class': 'form', 'pattern': '^(\d{11}$', 'title':'99999999999'}),
                   'lastName': TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Celular', 'class': 'form', 'pattern': '^(\+\d{2})?\d{12}$', 'title':'031999999999'}),
                   'cellPhone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?\d{12}$', 'title':'031999999999'}),
                   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                   'address': TextInput(attrs={'placeholder': 'Endereço', 'class': 'form'}),
                   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete':'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete':'new-password'})
                   }

class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['firstName', 'fantasyName', 'email', 'phone','login',
                  'password']

        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
                   'fantasyName': TextInput(attrs={'placeholder': 'Nome Fantasia', 'class': 'form'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?\d{12}$', 'title':'031999999999'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete':'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete':'new-password'})
                   }

class MedicoForm(ModelForm):
	class Meta:
		model = Medico
		fields = ['firstName','cpf','crm', 'email', 'phone', 'cellPhone', 'city', 'address', 'street', 'login',
                   'password']
		widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form'}),
			   
			   'cpf': TextInput(attrs={'placeholder': 'CPF', 'class': 'form', 'pattern': '^(\d{11}$', 'title':'99999999999'}),
			   'crm': TextInput(attrs={'placeholder': 'CRD', 'class': 'form', 'pattern': '^(\d{10}$', 'title':'9999999999'}),
			   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
			   'phone': TextInput(attrs={'placeholder': 'Celular', 'class': 'form', 'pattern': '^(\+\d{2})?\d{12}$', 'title':'031999999999'}),
			   'cellPhone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?\d{12}$', 'title':'031999999999'}),
                   	   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                    	   'address': TextInput(attrs={'placeholder': 'Endereço', 'class': 'form'}),
                    	   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   	   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete':'new-login'}),
                   	   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete':'new-password'})
                    }

