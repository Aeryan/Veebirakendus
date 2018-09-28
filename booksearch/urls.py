from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.top, name='top')
]