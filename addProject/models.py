from django.db import models



from django.contrib.auth.models import User

class new_project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    # project_user_cr = models.CharField(max_length=30)
    def __str__(self):
        return self.project_name


class Projectapp(models.Model):
    #nazwa_projektu = models.CharField(max_length=30)
    nazwa_projektu = models.ForeignKey(new_project, on_delete=models.CASCADE)
    # print(request.user.username
    #tworcaProjektu_id = models.CharField(max_length=30)
    
    uzytkownik_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    role_choise = (
        ('Moderator', 'Moderator'),
        ('Menager', 'Menager'),
        ('User', 'User'),
        ('Person', 'Person'),
    )
    rola = models.CharField(max_length=30, blank=True, null=True, choices=role_choise)


class displayusername(models.Model):
    username=models.CharField(max_length=100)
