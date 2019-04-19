from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':_('First name')}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':_('Last name')}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':_('Email address')}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':_('Password')}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':_('Confirm password')}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
