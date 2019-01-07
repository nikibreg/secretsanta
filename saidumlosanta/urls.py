from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^newgroup/$', views.newgroup.as_view(), name='newgroup'),
]