from django import forms
from django.contrib.auth.models import User
from .models import Projectapp
from .models import new_project

class new_project_form(forms.ModelForm):
    class Meta:
        model = new_project
        fields = ['project_name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projectapp
        fields = ['nazwa_projektu', 'uzytkownik_id','rola']
    # tworcaProjektu = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.all(),
    #     # widget=forms.CheckboxSelectMultiple
    # )