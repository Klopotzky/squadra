from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    project_creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.project_name


class ProjectUser(models.Model):
    nazwa_projektu = models.ForeignKey(Project, on_delete=models.CASCADE)
    uzytkownik_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    role_choise = (
        ('Moderator', 'Moderator'),
        ('Menager', 'Menager'),
        ('User', 'User'),
        ('Person', 'Person'),
    )
    rola = models.CharField(max_length=30, blank=True, null=True, choices=role_choise)

