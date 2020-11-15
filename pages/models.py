from django.db import models


# Create your models here.

class Pages(models.Model):
    title = models.CharField(max_length=200)
    rok = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)


def __str__(self):
    return self.title
