import django_filters
from django_filters import OrderingFilter

from big_filter.models import Studies, Modalities


# https://django-filter.readthedocs.io/en/stable/guide/usage.html
class StudiesFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='gt')
    patient_fio = django_filters.CharFilter(lookup_expr='icontains')
   

    class Meta:
        model = Studies
        ordering = ('patient_fio',)
        fields = ['patient_fio', 'id']
