from django import forms


class Signup(forms.Form):
    k_nimi = forms.CharField(label='Kasutajanimi', max_length=50)
    parool = forms.CharField(label='Parool', max_length=30)
