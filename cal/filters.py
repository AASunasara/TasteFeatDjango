from .models import item_preparation_detail, factorylog, note, item, worker
import django_filters
from django_filters import DateRangeFilter, DateFilter , ModelChoiceFilter, ModelMultipleChoiceFilter
from django import forms
from django.forms import DateField
from datetime import date, datetime

class ItemsFilter(django_filters.FilterSet):
    item_id = ModelChoiceFilter(queryset = item.objects.all(), label='Item Name')
    worker_id = ModelChoiceFilter(queryset = worker.objects.all(), label='Worker Name')
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = item_preparation_detail
        fields = ['date', 'item_id', 'worker_id']

class FactoryLogFilter(django_filters.FilterSet):
    # start_date = ModelChoiceFilter(queryset = factorylog.objects.dates('date', 'day'), lookup_expr=('gt'))
    # end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    # date = ModelChoiceFilter(queryset = factorylog.objects.dates('date', 'day'), label = 'Date')
    # factorylog_id = ModelChoiceFilter(queryset = factorylog.objects.all(), label = 'Date')
    # start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    # date = ModelChoiceFilter(queryset = factorylog.objects.values_list('date'), label = 'Date')
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    class Meta:
        model = factorylog
        fields = ['date']