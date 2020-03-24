from django import forms
from .models import factorylog, items, notes
from django.contrib.auth.models import User
from django.forms import DateField 
from datetime import date, datetime
from django.conf import settings

class ItemsForm(forms.ModelForm):
    rweight = forms.FloatField(min_value=0.0)
    iweight = forms.FloatField(min_value=0.0 )

    class Meta:
        model = items
        fields = ['date', 'item_names', 'rweight', 'iweight', 'grade', 'worker', 'note']


class FactoryLogForm(forms.ModelForm):
    class Meta:
        model = factorylog
        fields = ['date', 'fact_open_time', 'fact_close_time']


class Notes(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['setup', 'cleansing']