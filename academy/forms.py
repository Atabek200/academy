from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Master, Specialization


class MasterSignUpForm(UserCreationForm):
    contact_phone = forms.CharField(max_length=15)
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all())
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact_phone', 'specialization', 'photo')


class ClientSignUpForm(UserCreationForm):
    contact_phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact_phone', 'address')


