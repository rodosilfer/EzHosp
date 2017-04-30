from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'lastName', 'email', 'phone', 'cellPhone', 'city', 'address', 'street', 'login',
                  'password']

        widgets = {'firstName': TextInput(attrs={'placeholder': 'Primeiro Name', 'class': 'form'}),
                   'lastName': TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form'}),
                   'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form'}),
                   'phone': TextInput(attrs={'placeholder': 'Celular', 'class': 'form', 'pattern': '^(\+\d{2})?\d{11}$', 'title':'+5531999999999'}),
                   'cellPhone': TextInput(attrs={'placeholder': 'Telefone', 'class': 'form', 'pattern': '^(\+\d{2})?\d{11}$', 'title':'+5531999999999'}),
                   'city': TextInput(attrs={'placeholder': 'Cidade', 'class': 'form'}),
                   'address': TextInput(attrs={'placeholder': 'Endereço', 'class': 'form'}),
                   'street': TextInput(attrs={'placeholder': 'Rua', 'class': 'form'}),
                   'login': TextInput(attrs={'placeholder': 'Login', 'class': 'form', 'autocomplete':'new-login'}),
                   'password': PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form', 'autocomplete':'new-password'})
                   }
