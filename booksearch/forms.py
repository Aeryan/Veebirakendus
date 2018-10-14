from django import forms


class Login(forms.Form):
    login_k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                             error_messages={'invalid': "Kasutajanimi on juba võetud!"})
    login_parool = forms.CharField(label='Parool', max_length=30)


class Signup(forms.Form):
    signup_k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                             error_messages={'invalid': "Kasutajanimi on juba võetud!"})
    signup_parool = forms.CharField(label='Parool', max_length=30)


class Search(forms.Form):
    otsing = forms.CharField(label='Otsing', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Kirjuta siia, mida soovid otsida'}))
