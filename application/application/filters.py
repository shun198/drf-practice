import django_filters
from django.db.models import Q
from django.db.models.functions import Concat

from application.models import Customer


def get_address(queryset, address_query):
    """address_queryで取得した住所に該当するquerysetを取得
    Args:
        queryset
        address_query
    Returns:
        queryset: address_queryで取得した都道府県・市区町村・番地・その他に該当するqueryset
    """
    return queryset.annotate(
        address=Concat(
            "customer__address__prefecture",
            "customer__address__municipalities",
            "customer__address__house_no",
            "customer__address__post_no",
            "customer__address__other",
        )
    ).filter(icontains=address_query)


class CustomerFilter(django_filters.FilterSet):
    """お客様名を氏名・カナ氏名両方で絞り込むFilter
    Args:
        django_filters
    """

    name = django_filters.CharFilter(method="search_name", label="name")
    address = django_filters.CharFilter(method="search_address")

    class Meta:
        model = Customer
        fields = ["name", "address"]

    def search_name(self, queryset, name, value):
        return queryset.filter(
            Q(name__contains=value) | Q(kana__contains=value)
        )

    def search_address(self, queryset, address, value):
        return get_address(queryset=queryset, address_query=value)
