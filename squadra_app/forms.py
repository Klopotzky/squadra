from django import forms
from .models import Tekst_a, Pliki


class TekstForm(forms.ModelForm):
    class Meta:
        model = Tekst_a
        # fields = ('title', 'text_app', )
        fields = ('text_app',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Pliki
        fields = ('sciezka',)


class NewFileForm(forms.ModelForm):
    class Meta:
        model = Pliki
        fields = ('sciezka',)
