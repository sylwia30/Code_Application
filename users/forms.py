from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Imię:', required=False)
    last_name = forms.CharField(label='Nazwisko:', required=False)
    username = forms.CharField(label='Nick:')
    email = forms.EmailField(required=True, label='E-mail:')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Hasło:')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Powtórz hasło:')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')

    class Meta:
        model = User
        fields = ['email', 'password']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię:', required=False)
    last_name = forms.CharField(label='Nazwisko:', required=False)
    username = forms.CharField(label='Nick:', required=False)
    email = forms.EmailField(label='E-mail:', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
