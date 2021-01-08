from django.db import models
from django.contrib.auth.models import User
from addProject.models import Project


class Board(models.Model):
    position = models.PositiveSmallIntegerField(blank=False, default=1)
    id_user = models.ForeignKey(User, blank=True, null=True, related_name='%(class)s_requests_user',
                                on_delete=models.SET_NULL)
    id_creator = models.ForeignKey(User, blank=False, null=False, related_name='%(class)s_requests_creator',
                                   on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True, max_length=1024)
    priority = models.CharField(max_length=30, blank=True, null=True)
    creation_time = models.DateTimeField()
    modification_timee = models.DateTimeField()
    description = models.TextField(blank=True, null=True, max_length=1024)
