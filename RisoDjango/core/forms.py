from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Usuario:',
            'password': 'Senha:',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Digite seu usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder':'Digite sua senha'}),
        }
        error_messages = {
            'usuario': {
                'required': ("Informe o usuario."),
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise ValidationError("Usuário não encontrado.")

            user = authenticate(username=user.username, password=password)
            if user is None:
                raise ValidationError("Senha incorreta para o usuario informado.")

            self.user = user