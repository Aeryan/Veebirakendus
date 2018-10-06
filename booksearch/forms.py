from django import forms


class Signup(forms.Form):
    k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                             error_messages={'invalid': "Kasutajanimi on juba võetud!"})
    parool = forms.CharField(label='Parool', max_length=30)


class Search(forms.Form):
    otsing = forms.CharField(label='Otsing', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Kirjuta siia, mida soovid otsida'}))
