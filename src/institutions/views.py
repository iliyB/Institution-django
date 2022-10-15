from typing import Dict

from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from institutions.models import Institution
from institutions.serializers import InstitutionListSerializer, InstitutionRetrieveSerializer


class InstitutionRetrieveView(RetrieveAPIView):
    model = Institution
    queryset = Institution.objects.select_related("enterprise_network").prefetch_related("products", "districts").all()
    serializer_class = InstitutionRetrieveSerializer


class InstitutionListView(ListAPIView):
    model = Institution
    queryset = Institution.objects.select_related("enterprise_network").all()
    serializer_class = InstitutionListSerializer

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(districts__id=self.kwargs.get("district_pk"))

        return self._queryset_filter(queryset, self.request.query_params)

    @staticmethod
    def _queryset_filter(queryset: QuerySet, query_params: Dict) -> QuerySet:
        if query_params.get("category"):
            try:
                queryset = queryset.filter(products__category__id__in=query_params.get("category").split(","))  # type: ignore
            except:
                pass
        if query_params.get("product_title"):
            try:
                queryset = queryset.filter(products__title__icontains=query_params.get("product_title"))
            except:
                pass
        if query_params.get("min_price"):
            try:
                queryset = queryset.filter(
                    productinstitutionassociated__price__gte=float(query_params.get("min_price"))  # type: ignore
                )
            except:
                pass
        if query_params.get("max_price"):
            try:
                queryset = queryset.filter(
                    productinstitutionassociated__price__lte=float(query_params.get("max_price"))  # type: ignore
                )
            except:
                pass

        return queryset.distinct()
