import django_filters
from models import Name

class NameFilter(django_filters.FilterSet):
    min_price = django_filters.CharFilter(lookup_type='icontains')
    class Meta:
        model = Name
        fields = ('name',)