from django.http import HttpResponseRedirect, HttpResponse
from .forms import Login, Signup, Search, AddOwned, AddWanted
from .models import raamatud, owned, wanted
from django.db import IntegrityError, connection
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import bcrypt

salt = b'$2b$12$46cw2.wl5erIKwdMTQqeF.'


def about(request):
    loginform = Login(None or request.POST)
    signupform = Signup(None or request.POST)

    if loginform.is_valid():
        login_name = loginform.cleaned_data['login_k_nimi']
        login_password = bcrypt.hashpw(loginform.cleaned_data['login_parool'].encode(), salt).decode()
        user = authenticate(request, username=login_name, password=login_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')

    if signupform.is_valid():
        signup_name = signupform.cleaned_data['signup_k_nimi']
        signup_password = bcrypt.hashpw(signupform.cleaned_data['signup_parool'].encode(), salt).decode()
        user = User.objects.create_user(signup_name, password=signup_password)
        try:
            user.save()
        except IntegrityError:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('')

    return render(request, 'booksearch/About.html', {'loginform': loginform, 'signupform': signupform})


def search(request):
    loginform = Login(None or request.POST)
    signupform = Signup(None or request.POST)
    ownedform = AddOwned(None or request.POST)
    wantedform = AddWanted(None or request.POST)

    if loginform.is_valid():
        login_name = loginform.cleaned_data['login_k_nimi']
        login_password = bcrypt.hashpw(loginform.cleaned_data['login_parool'].encode(), salt).decode()
        user = authenticate(request, username=login_name, password=login_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')

    if signupform.is_valid():
        signup_name = signupform.cleaned_data['signup_k_nimi']
        signup_password = bcrypt.hashpw(signupform.cleaned_data['signup_parool'].encode(), salt).decode()
        user = User.objects.create_user(signup_name, password=signup_password)
        try:
            user.save()
            HttpResponseRedirect('')
        except IntegrityError:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('')

    if ownedform.is_valid():
        omatud_pealkiri = ownedform.cleaned_data['omatu_pealkiri']
        raamat = raamatud.objects.get(pealkiri=omatud_pealkiri)
        omatud = owned(usr=request.user.id, book_id=raamat.id, comment="")
        try:
            omatud.save()
            HttpResponseRedirect('')
        except IntegrityError:
            HttpResponseRedirect('')

    if wantedform.is_valid():
        tahetud_pealkiri = wantedform.cleaned_data['tahetu_pealkiri']
        raamat = raamatud.objects.get(pealkiri=tahetud_pealkiri)
        tahetud = wanted(usr=request.user.id, book_id=raamat.id, comment="")
        try:
            tahetud.save()
            HttpResponseRedirect('')
        except IntegrityError:
            HttpResponseRedirect('')

    sisend = request.session.get('sisend')
    if sisend is None:
        return HttpResponseRedirect('/')
    tulem = raamatud.objects.filter(pealkiri__icontains=sisend)
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM booksearch_raamatud WHERE pealkiri ILIKE '%" + sisend + "%'")
    arv = cursor.fetchone()[0]

    if arv == 1:
        sone = 'Leiti 1 tulemus'
    else:
        sone = 'Leiti ' + str(arv) + ' tulemust'
    return render(request, 'booksearch/Search.html',
                  {'nimistik': tulem, 'loginform': loginform,
                   "signupform": signupform, 'tulemuste_sone': sone,
                   'ownedform': ownedform, 'wantedform': wantedform})


def signout(request):
    sisend = request.session.get('sisend')
    logout(request)
    request.session['sisend'] = sisend
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def mylists(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    else:
        soovid = raamatud.objects.filter(wanted__usr=request.user.id)
        olemas = raamatud.objects.filter(owned__usr=request.user.id)
        return render(request, 'booksearch/MyLists.html', {'olemas': olemas, 'soovid': soovid})


def index(request):

    if request.method == 'POST':
        loginform = Login(None or request.POST)
        signupform = Signup(None or request.POST)
        search = Search(None or request.POST)

        if loginform.is_valid():
            login_name = loginform.cleaned_data['login_k_nimi']
            login_password = bcrypt.hashpw(loginform.cleaned_data['login_parool'].encode(), salt).decode()
            user = authenticate(request, username=login_name, password=login_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('')

        if signupform.is_valid():
            signup_name = signupform.cleaned_data['signup_k_nimi']
            signup_password = bcrypt.hashpw(signupform.cleaned_data['signup_parool'].encode(), salt).decode()
            user = User.objects.create_user(signup_name, password=signup_password)
            try:
                user.save()
            except IntegrityError:
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('')

        if search.is_valid():
            request.session['sisend'] = search.cleaned_data['otsing']
            return redirect('search')

    else:
        loginform = Login
        signupform = Signup
        search = Search
    return render(request, 'booksearch/Frontpage.html', {'loginform': loginform, 'signupform': signupform,
                                                         'search': search})

