from django.http import HttpResponseRedirect
from .forms import Login, Signup, Search
from .models import raamatud
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
import bcrypt
from django.contrib.auth.models import User

salt = b'$2b$12$46cw2.wl5erIKwdMTQqeF.'


def about(request):
    return render(request, 'booksearch/About.html')


'''
def search(request):
    if request.method == 'POST':
        search = Search(request.POST)
'''


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


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
                return render(request, 'booksearch/Frontpage.html', {'loginform': loginform, 'signupform': signupform,
                                                                     'search': search, 'user':user})
        if signupform.is_valid():
            signup_name = signupform.cleaned_data['signup_k_nimi']
            signup_password = bcrypt.hashpw(signupform.cleaned_data['signup_parool'].encode(), salt).decode()
            user = User.objects.create_user(signup_name, password=signup_password)
            try:
                user.save()
            except IntegrityError:
                return HttpResponseRedirect('')
            return HttpResponseRedirect('')

        if search.is_valid():
            sisend = search.cleaned_data['otsing']
            tulem = raamatud.objects.filter(pealkiri__icontains=sisend)
            return render(request, 'booksearch/Search.html', {'nimistik': tulem, 'loginform': loginform,
                                                              "signupform": signupform})

    else:
        loginform = Login
        signupform = Signup
        search = Search
    return render(request, 'booksearch/Frontpage.html', {'loginform': loginform, 'signupform': signupform,
                                                         'search': search})

