from django import forms
from django.contrib.auth.models import User
from .models import ProjectUser
from .models import Project


class new_project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name',]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        # tworcaProjektu_id = 'ss'
        fields = ['nazwa_projektu', 'uzytkownik_id', 'rola']

    # tworcaProjektu = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.all(),
    #     # widget=forms.CheckboxSelectMultiple
    # )
