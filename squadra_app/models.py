from django.db import models
from ckeditor.fields import RichTextField


class Tekst_a(models.Model):
    # title = models.CharField(max_length=200)
    text_app = RichTextField(blank=True, null=True)

    # def __str__(self):
    #   return self.title


# class Katalog(models.Model):
#     # id_projektu = models.ForeignKey(Projekty)
#     id_katalogu_nadrzednego = models.IntegerFields()
#
#
# class Pliki(models.Model):
#     id_katalogu = models.ForeignKey(Katalog)
#     # id_user = models.ForeignKey(user_id)
