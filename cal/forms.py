from django import forms
from .models import days, items
from django.contrib.auth.models import User
from django.forms import DateField
from datetime import date, datetime
from datetime import date
from django.conf import settings

class ItemsForm(forms.ModelForm):
    rweight = forms.FloatField(min_value=0.0)
    iweight = forms.FloatField(min_value=0.0 )

    class Meta:
        model = items
        fields = ['item_names', 'rweight', 'iweight', 'grade', 'worker', 'note']


class DaysForm(forms.ModelForm):
    class Meta:
        model = days
        fields = ['date', 'fact_open_time', 'fact_close_time', 'setup', 'cleansing']
