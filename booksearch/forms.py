from django import forms


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


class AddOwned(forms.Form):
    omatu_pealkiri = forms.CharField(label='Olemasoleva pealkiri', max_length=50, required=True,
                                     widget=forms.HiddenInput(attrs={'id': 'ownedField'}))


class AddWanted(forms.Form):
    tahetu_pealkiri = forms.CharField(label='Tahetu pealkiri', max_length=50, required=True,
                                      widget=forms.HiddenInput(attrs={'id': 'wantedField'}))


class RemoveWanted(forms.Form):
    tahtmatu_pealkiri = forms.CharField(label='Tahtmatu pealkiri', max_length=50, required=True,
                                        widget=forms.HiddenInput(attrs={'id': 'wantedField'}))


class addBook(forms.Form):
    pealkiri = forms.CharField(label='Pealkiri', max_length=50, required=True)
    autor = forms.CharField(label='Autor', max_length=30, required=True)
    kirjastus = forms.CharField(label='Kirjastus', max_length=30, required=True)
    ilmumisaasta = forms.IntegerField(required=True)
    lehekülgi = forms.IntegerField(required=True)
    keel = forms.CharField(max_length=10, required=True)
    pilt = forms.ImageField(required=False,
                            widget=forms.FileInput(attrs={'type': 'file',
                                                          'name': 'bookCover'}))
