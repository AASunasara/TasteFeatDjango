from .models import item_preparation_detail, factorylog, note, item, worker
import django_filters
from django_filters import DateRangeFilter, DateFilter 
from django import forms
from django.forms import DateField
from datetime import date, datetime

class ItemsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = item_preparation_detail
        fields = ['date']

class FactoryLogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = factorylog
        fields = ['date']