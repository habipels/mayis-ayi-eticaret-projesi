from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def index(request):
    urun = urunler.objects.all()[:4]
    kategoriler = kategori.objects.all()
    sozluk = {"urun":urun,"kategoriler":kategoriler}
    return render(request,"index_temps/index.html",sozluk)

def kategorii(request,id,slug):
    urun = urunler.objects.filter(id = id)
    kategoriler = kategori.objects.all()
    gidece_veri = id
    sozluk = {"urun":urun,"kategoriler":kategoriler,"gidece_veri":gidece_veri}
    return render(request,"index_temps/index.html",sozluk)

