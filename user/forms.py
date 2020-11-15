from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UserRegister(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',  'email', 'first_name', 'last_name', 'password1', 'password2']


# class AccountAuth(forms.ModelForm):

#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = Account
#         fields = ('email', 'password')

#     def clean(self):
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#         if not authenticate(email=email, password=password):
#             raise forms.ValidationError('zle logowanie')