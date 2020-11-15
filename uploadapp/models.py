from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='pliki/')
    title = models.CharField(max_length=50, default=" ")
