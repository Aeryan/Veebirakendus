from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/$', views.about),
    # path('/search', views.search),
    path('signout', views.signout, name='signout'),
    path('', views.index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
