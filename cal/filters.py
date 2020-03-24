from .models import items, factorylog, notes
import django_filters
from django_filters import DateRangeFilter, DateFilter 
from django import forms
from django.forms import DateField
from datetime import date, datetime

class ItemsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = items
        fields = ['date', 'worker', 'item_names', 'grade']

class FactoryLogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = factorylog
        fields = ['date']