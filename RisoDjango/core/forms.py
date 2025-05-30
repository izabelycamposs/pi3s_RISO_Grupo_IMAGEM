from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário",
            }
        ),
        error_messages={"required": "Informe o usuário."},
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ),
        error_messages={"required": "Informe a senha."},
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise ValidationError("Usuário ou senha inválidos.")
            if not user.is_active:
                raise ValidationError("Usuário inativo, entre em contato com o administrador.")

            self.user = user

        return cleaned_data
