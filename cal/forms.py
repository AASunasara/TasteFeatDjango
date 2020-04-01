from django import forms
from .models import item_preparation_detail, factorylog, note, item, worker
from django.contrib.auth.models import User
from django.forms import DateField 
from datetime import date, datetime
from django.conf import settings

class ItemPreForm(forms.ModelForm):
    rweight = forms.FloatField(min_value=0.0)
    class Meta:
        model = item_preparation_detail
        fields = ['rweight', 'note', 'grade', 'date']


class FactoryLogForm(forms.ModelForm):
    class Meta:
        model = factorylog
        fields = ['date', 'fact_open_time', 'fact_close_time']


class NoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ['setup', 'cleansing']