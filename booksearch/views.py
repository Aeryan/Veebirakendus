from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signup
from .models import kasutajad
from django.db import IntegrityError
import bcrypt

salt = b'$2b$12$46cw2.wl5erIKwdMTQqeF.'

def about(request):
    return HttpResponse('templates/booksearch/About')

def index(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['k_nimi']
            password = bcrypt.hashpw(form.cleaned_data['parool'].encode(), salt).decode()
            p = kasutajad(kasutajanimi=name, parool=password)
            try:
                p.save()
            except IntegrityError:
                return HttpResponseRedirect('')
            return HttpResponseRedirect('')
    else:
        form = Signup
    return render(request, 'booksearch/Frontpage.html', {'form': form})

