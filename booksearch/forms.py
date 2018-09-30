from django import forms
from django.contrib.auth.models import User


class Signup(forms.ModelForm):
    k_nimi = forms.CharField(label='Kasutajanimi', max_length=50,
                             error_messages={"Kasutajanimi on juba võetud!"})
    parool = forms.CharField(label='Parool', max_length=30)

    class Meta:
        model = User

    def clean_username(self):
        username = self.cleaned_data["k_nimi"]

        try:
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username'
            )
        except User.DoesNotExist:
            return username