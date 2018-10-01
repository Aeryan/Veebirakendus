from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Signup
from .models import kasutajad
import os
import psycopg2


def index(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            name = form.cleaned_data['k_nimi']
            password = form.cleaned_data['parool']
            p = kasutajad(kasutajanimi=name, parool=password)
            p.save()
            return HttpResponseRedirect('')
    else:
        form = Signup
    return render(request, 'booksearch/Frontpage.html', {'form': form})


def top(request):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Raamatud;")
    book = cur.fetchone()
    cur.close()
    conn.close()
    html = "<html><body>Top1 raamat on %s.</body></html>" % book[1]
    return HttpResponse(html)
