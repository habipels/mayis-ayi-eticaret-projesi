from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class kategori(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim

class urunler(models.Model):
    kategorim = models.ForeignKey(kategori,on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    fiyat = models.BigIntegerField()
    stok = models.BigIntegerField()
    urun_resim = models.FileField(upload_to='urun_resim/',blank = True,null = True)
    aciklama = RichTextField(null = True)
    def __str__(self) :
        return self.isim