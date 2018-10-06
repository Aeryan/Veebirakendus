from django.http import HttpResponseRedirect
from .forms import Signup, Search
from .models import kasutajad, raamatud
from django.db import IntegrityError
from django.shortcuts import render
import bcrypt

salt = b'$2b$12$46cw2.wl5erIKwdMTQqeF.'


def about(request):
    return render(request, 'booksearch/About.html')


'''
def search(request):
    if request.method == 'POST':
        search = Search(request.POST)
'''


def index(request):

    if request.method == 'POST':
        form = Signup(request.POST)
        search = Search(request.POST)
        if form.is_valid():
            name = form.cleaned_data['k_nimi']
            password = bcrypt.hashpw(form.cleaned_data['parool'].encode(), salt).decode()
            p = kasutajad(kasutajanimi=name, parool=password)
            try:
                p.save()
            except IntegrityError:
                return HttpResponseRedirect('')
            return HttpResponseRedirect('')

        if search.is_valid():
            sisend = search.cleaned_data['otsing']
            tulem = raamatud.objects.filter(pealkiri__icontains=sisend)
            return render(request, 'booksearch/Search.html', {'nimistik': tulem})

    else:
        form = Signup
        search = Search
    return render(request, 'booksearch/Frontpage.html', {'form': form, 'search': search})

