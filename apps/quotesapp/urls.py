from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'quotes'
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^registrationLogin/$', views.registration_login, name="registration_login"),
    url(r'^registration/$', views.registration, name="registration"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout")
]