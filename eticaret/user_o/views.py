from django.shortcuts import render,HttpResponse , redirect
from .forms import *
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
def giris(request):
    formlarimiz = login_form(request.POST or None)
    sozluk = {"forms":formlarimiz}
    if formlarimiz.is_valid():
        username = formlarimiz.cleaned_data.get("usernamee")
        password = formlarimiz.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            return render(request,"user_op_temps/login.html",sozluk)
        login(request,user)
        return redirect("index")
    return render(request,"user_op_temps/login.html",sozluk)
def kayit(request):
    formlarim = register_forms(request.POST or None)
    if formlarim.is_valid():
        username = formlarim.cleaned_data.get("username")
        password = formlarim.cleaned_data.get("password")
        email = formlarim.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("index")
    sozluk = {
            "forms" : formlarim
        }
    return render(request,"user_op_temps/register.html",sozluk)
def cikis(request):
    logout(request)
    return redirect("index")

def ortak(request):
    kayilar = register_forms(request.POST or None)
    if kayilar.is_valid():
        username = kayilar.cleaned_data.get("username")
        password = kayilar.cleaned_data.get("password")
        email = kayilar.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("index")
    
    formlarimiz = login_form(request.POST or None)
    sozluk = {
            "kayilar" : kayilar,"forms":formlarimiz
        }
    if formlarimiz.is_valid():
        username = formlarimiz.cleaned_data.get("usernamee")
        password = formlarimiz.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            return render(request,"user_op_temps/ortak.html",sozluk)
        login(request,user)
        return redirect("index")
    return render(request,"user_op_temps/ortak.html",sozluk)
