from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signup
from .models import kasutajad
from django.db import IntegrityError

def index(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            name = form.cleaned_data['k_nimi']
            password = form.cleaned_data['parool']
            p = kasutajad(kasutajanimi=name, parool=password)
            try:
                p.save()
            except IntegrityError:
                return HttpResponseRedirect('')
            return HttpResponseRedirect('')
    else:
        form = Signup
    return render(request, 'booksearch/Frontpage.html', {'form': form})

