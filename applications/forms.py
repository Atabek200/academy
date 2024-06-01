from django import forms
from .models import Application
from academy.models import Master


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'message', 'master']

    master = forms.ModelChoiceField(queryset=Master.objects.all(), label="Choose a Master")
