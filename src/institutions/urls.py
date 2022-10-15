from typing import List

from django.urls import path

from institutions.views import InstitutionListView, InstitutionRetrieveView

urlpatterns: List = [
    path("district/<int:district_pk>", InstitutionListView.as_view(), name="institution_list_view"),
    path("<int:pk>", InstitutionRetrieveView.as_view(), name="institution_retrieve_view"),
]
