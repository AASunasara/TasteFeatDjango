from django import forms
from .models import days, items
from django.contrib.auth.models import User


class ItemsForm(forms.ModelForm):


    class Meta:
        model = items
        fields = ['item_names', 'rweight', 'iweight', 'grade', 'worker', 'note']


class DaysForm(forms.ModelForm):
    class Meta:
        model = days
        fields = ['date', 'fact_open_time', 'fact_close_time', 'setup', 'cleansing']
