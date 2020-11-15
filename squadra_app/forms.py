from django import forms
from .models import Tekst_a


class TekstForm(forms.ModelForm):
    class Meta:
        model = Tekst_a
        # fields = ('title', 'text_app', )
        fields = ('text_app',)
