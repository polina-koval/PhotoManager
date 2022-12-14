import django_filters
from django_filters.widgets import RangeWidget

from photo.models import Photo


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class PhotoFilter(django_filters.FilterSet):
    people = CharInFilter(lookup_expr="overlap")
    date = django_filters.DateFromToRangeFilter(
        widget=RangeWidget(attrs={"type": "date"})
    )

    class Meta:
        model = Photo
        fields = {"location": ["icontains"], "date": [], "people": []}
