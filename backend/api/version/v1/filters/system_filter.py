import django_filters
from log.models import Log

# https://django-filter.readthedocs.io/en/stable/ref/filters.html#core-arguments


class HistoryLogFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user", lookup_expr="icontains")
    method = django_filters.CharFilter(field_name="method", lookup_expr="icontains")
    action = django_filters.filters.MultipleChoiceFilter(
        field_name="action", choices=Log.Action.choices
    )
    level = django_filters.filters.MultipleChoiceFilter(
        field_name="level", choices=Log.Level.choices
    )
    info = django_filters.CharFilter(field_name="info", lookup_expr="icontains")
    created = django_filters.IsoDateTimeFromToRangeFilter(field_name="created")

    class Meta:
        model = Log
        fields = ["user", "method", "action", "level", "info", "created"]
