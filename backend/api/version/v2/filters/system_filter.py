import django_filters
from django.contrib.auth.models import User
from base.models import Profile


# https://django-filter.readthedocs.io/en/stable/ref/filters.html#core-arguments


class MyFilter(django_filters.FilterSet):
    username_fed = django_filters.CharFilter(field_name="username", lookup_expr="icontains")
    first_name_fed = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    gender_fed = django_filters.filters.MultipleChoiceFilter(
        field_name="profile__gender", choices=Profile.Gender.choices
    )
    # method = django_filters.CharFilter(field_name="method", lookup_expr="icontains")
    # action = django_filters.filters.MultipleChoiceFilter(
    #     field_name="action", choices=Log.Action.choices
    # )
    # level = django_filters.filters.MultipleChoiceFilter(
    #     field_name="level", choices=Log.Level.choices
    # )
    # info = django_filters.CharFilter(field_name="info", lookup_expr="icontains")
    # created = django_filters.IsoDateTimeFilter(field_name="profile__created")

    created = django_filters.IsoDateTimeFromToRangeFilter(field_name="profile__created")

    class Meta:
        model = User
        fields = ["username_fed", "first_name_fed", "gender_fed"]
