from django import forms
from django.forms import HiddenInput


class Login(forms.Form):
    login_k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                                   error_messages={'invalid': "Kasutajanimi on juba võetud!"},
                                   widget=forms.TextInput(attrs={'class': 'loginfield'}))
    login_parool = forms.CharField(label='Parool', max_length=30, widget=forms.TextInput(attrs={'class': 'loginfield'}))


class Signup(forms.Form):
    signup_k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                                    error_messages={'invalid': "Kasutajanimi on juba võetud!"},
                                    widget=forms.TextInput(attrs={'class': 'signupfield'}))
    signup_parool = forms.CharField(label='Parool', max_length=30,
                                    widget=forms.TextInput(attrs={'class': 'signupfield'}))


class Search(forms.Form):
    otsing = forms.CharField(label='Otsing', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Otsing',
                                                           'class': 'searchfield'}))


class AddOwned(forms.ModelForm):
    class Meta:
        widgets = {'any_field': HiddenInput(), }
