from django.http import HttpResponseRedirect
from .forms import Login, Signup, Search, AddOwned, AddWanted, RemoveWanted, addBook
from .models import raamatud, owned, wanted, tracking
from django.db import IntegrityError, connection
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import matplotlib.pyplot as plt
import datetime


def add_to_tracking(request):
    ip = request.META.get('REMOTE_ADDR')
    browser = request.user_agent.browser.family
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # '2004-10-19 10:23:54'
    opsys = request.user_agent.os.family

    timetable = tracking(ip=ip, brauser=browser, time=time, os=opsys)
    timetable.save()


def addition(request):
    additionform = addBook(None or request.POST, None or request.FILES)
    error = ""
    if request.method == "POST":
        if additionform.is_valid():
            pealkiri = additionform.cleaned_data['pealkiri']
            autor = additionform.cleaned_data['autor']
            kirjastus = additionform.cleaned_data['kirjastus']
            ilmumisaasta = additionform.cleaned_data['ilmumisaasta']
            lk = additionform.cleaned_data['lehekülgi']
            keel = additionform.cleaned_data['keel']
            try:
                raamatud.objects.get(pealkiri=pealkiri)
                error = "See raamat on juba olemas!"
            except ObjectDoesNotExist:
                raamat = raamatud.objects.create(pealkiri=pealkiri, autor=autor,
                                                 kirjastus=kirjastus,
                                                 ilmumisaasta=ilmumisaasta,
                                                 lehekülgi=lk, keel=keel)
                raamat.save()

                if request.FILES.get('pilt') is not None:
                    pilt = request.FILES.get('pilt')
                    fs = FileSystemStorage()
                    fs.save(pealkiri + "." + pilt.name.split('.')[1], pilt)
                return HttpResponseRedirect('')

    return render(request, 'booksearch/Add.html', {'additionform': additionform,
                                                   'error': error})


def about(request):
    access_times = []
    for i in tracking.objects.values_list('time'):
        access_times.append(float(i[0].strftime('%H.%M')))
    plt.hist(access_times, range=[0.0, 24.0], bins=24, align='left')
    plt.savefig('static/booksearch/hittimes.png', bbox_inches='tight')
    plt.clf()

    loginform = Login(None or request.POST)
    signupform = Signup(None or request.POST)

    if loginform.is_valid():
        login_name = loginform.cleaned_data['login_k_nimi']
        login_password = loginform.cleaned_data['login_parool']
        user = authenticate(request, username=login_name, password=login_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')

    if signupform.is_valid():
        signup_name = signupform.cleaned_data['signup_k_nimi']
        signup_password = signupform.cleaned_data['signup_parool']
        user = User.objects.create_user(signup_name, password=signup_password)
        try:
            user.save()
            user_auth = authenticate(request, username=signup_name, password=signup_password)
            login(request, user_auth)
        except IntegrityError:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('')

    ip = request.META.get('REMOTE_ADDR')
    browser = request.user_agent.browser.family
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    opsys = request.user_agent.os.family

    browser_list = tracking.objects.values_list('brauser').distinct()
    browser_data = []
    for i in browser_list:
        browser_data.append([tracking.objects.filter(brauser=i[0]).count(), i[0]])
    browser_data = sorted(browser_data, reverse=True)

    os_list = tracking.objects.values_list('os').distinct()
    os_data = []
    for i in os_list:
        os_data.append([tracking.objects.filter(os=i[0]).count(), i[0]])
    os_data = sorted(os_data, reverse=True)

    return render(request, 'booksearch/About.html', {'loginform': loginform, 'signupform': signupform,
                                                     'ip': ip, 'browser': browser, 'time': time, 'os': opsys,
                                                     'browserdata': browser_data, 'osdata': os_data})


def search(request):
    loginform = Login(None or request.POST)
    signupform = Signup(None or request.POST)
    ownedform = AddOwned(None or request.POST)
    wantedform = AddWanted(None or request.POST)

    if loginform.is_valid():
        login_name = loginform.cleaned_data['login_k_nimi']
        login_password = loginform.cleaned_data['login_parool']
        user = authenticate(request, username=login_name, password=login_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')

    if signupform.is_valid():
        signup_name = signupform.cleaned_data['signup_k_nimi']
        signup_password = signupform.cleaned_data['signup_parool']
        user = User.objects.create_user(signup_name, password=signup_password)
        try:
            user.save()
            user_auth = authenticate(request, username=signup_name, password=signup_password)
            login(request, user_auth)
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
        rmwantedform = RemoveWanted(None or request.POST)
        soovid = raamatud.objects.filter(wanted__usr=request.user.id)
        olemas = raamatud.objects.filter(owned__usr=request.user.id)

        if rmwantedform.is_valid():
            tahtmatu_pealkiri = rmwantedform.cleaned_data['tahtmatu_pealkiri']
            raamat = raamatud.objects.get(pealkiri=tahtmatu_pealkiri)
            tahetud = wanted.objects.get(usr=request.user.id, book_id=raamat.id)
            try:
                tahetud.delete()
                HttpResponseRedirect('')
            except IntegrityError:
                HttpResponseRedirect('')

        return render(request, 'booksearch/MyLists.html', {'olemas': olemas, 'soovid': soovid,
                                                           'rmwantedform': rmwantedform})


def index(request):
    add_to_tracking(request)

    if request.method == 'POST':
        loginform = Login(None or request.POST)
        signupform = Signup(None or request.POST)
        searchform = Search(None or request.POST)

        if loginform.is_valid():
            login_name = loginform.cleaned_data['login_k_nimi']
            login_password = loginform.cleaned_data['login_parool']
            user = authenticate(request, username=login_name, password=login_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('')

        if signupform.is_valid():
            signup_name = signupform.cleaned_data['signup_k_nimi']
            signup_password = signupform.cleaned_data['signup_parool']
            user = User.objects.create_user(signup_name, password=signup_password)
            try:
                user.save()
                user_auth = authenticate(request, username=signup_name, password=signup_password)
                login(request, user_auth)
            except IntegrityError:
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('')

        if searchform.is_valid():
            request.session['sisend'] = searchform.cleaned_data['otsing']
            return redirect('search')

    else:
        loginform = Login
        signupform = Signup
        searchform = Search
    return render(request, 'booksearch/Frontpage.html', {'loginform': loginform, 'signupform': signupform,
                                                         'search': searchform})
