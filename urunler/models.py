from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    def __str__(self):
        return self.isim
class AltKategori(models.Model):
    isim = models.CharField(max_length=50)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.isim
class EnAlt(models.Model):
    isim = models.CharField(max_length=50)
    def __str__(self):
        return self.isim
class Urun(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True) # ManytoOne
    altkategoriler = models.ManyToManyField('AltKategori', blank=True)
    enalt = models.OneToOneField('EnAlt', on_delete=models.CASCADE, blank=True, null=True)
    isim = models.CharField(max_length=200)
    aciklama = models.TextField(max_length=500)
    fiyat = models.IntegerField()
    resim = models.FileField(upload_to = "urunler/", null = True, blank = True)

    def __str__(self):
        return self.isim