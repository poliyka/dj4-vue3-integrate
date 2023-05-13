from datetime import timedelta
import django_filters
from django.contrib.auth.models import User
from django.db.models import Count, F, Func, JSONField, Q, Value
from django.db.models.functions import Concat
from django.contrib.auth.models import Permission

# https://django-filter.readthedocs.io/en/stable/ref/filters.html#core-arguments


class UserListFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = self.queryset.annotate(
            name=Concat(F("last_name"), F("first_name")),
            rname=Concat(F("first_name"), F("last_name")),
        )

    account = django_filters.CharFilter(field_name="username", lookup_expr="icontains")
    name = django_filters.CharFilter(method="query_name_filter")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    is_active = django_filters.BooleanFilter(field_name="is_active")

    def query_name_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(rname__icontains=value))

    class Meta:
        model = User
        fields = ["name"]
