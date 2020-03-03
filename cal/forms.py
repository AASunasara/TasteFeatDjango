from django import forms
from .models import days, items
from django.contrib.auth.models import User


class ItemsForm(forms.ModelForm):
    rweight = forms.FloatField(min_value=0.0 )
    iweight = forms.FloatField(min_value=0.0 )


    class Meta:
        model = items
        fields = ['item_names', 'rweight', 'iweight', 'grade', 'worker', 'note']


class DaysForm(forms.ModelForm):
    # fact_open_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = days
        fields = ['date', 'fact_open_time', 'fact_close_time', 'setup', 'cleansing']
