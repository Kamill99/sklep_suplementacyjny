from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="Adres e-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Imię", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Nazwisko", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Login", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label="Stare hasło", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label="Nowe hasło", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label="Powtórz nowe hasło", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
