
from django.contrib import admin
from django.urls import path , include
from .views import *
app_name ="user"
urlpatterns = [
    path("login/",giris,name="login"),
    path("logout/",cikis,name="logout"),
    path("register/",kayit,name="register"),
    path("ortak/",ortak,name="ortak"),
]

