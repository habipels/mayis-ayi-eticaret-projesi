from django.shortcuts import render
from anasayfa.models import*
# Create your views here.
def detay(request,id,slug):
    urun = urunler.objects.get(id = id)
    sozluk = {"urun":urun}
    return render(request,"detay_temps/index.html",sozluk)