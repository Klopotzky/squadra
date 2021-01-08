from django.db import models
from ckeditor.fields import RichTextField


class Tekst_a(models.Model):
    # title = models.CharField(max_length=200)
    text_app = RichTextField(blank=True, null=True)

    # def __str__(self):
    #   return self.title


class Katalog(models.Model):
    # id_projektu = models.ForeignKey(Projekty)
    id_kat_nad = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    nazwa = models.CharField(max_length=124, default="Nowy Folder")

    def __str__(self):
        return self.nazwa


class Pliki(models.Model):
    id_katalogu = models.ForeignKey(Katalog, on_delete=models.CASCADE, blank=True, null=True)
    format = models.CharField(max_length=6)
    nazwa = models.CharField(max_length=256)
    sciezka = models.FileField(upload_to='pliki/', default="Nowy plik")
    # id_user = models.ForeignKey(user_id)

    def __str__(self):
        return self.id_katalogu
