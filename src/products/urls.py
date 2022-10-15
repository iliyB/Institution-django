from typing import List

from django.urls import path

from products.views import (
    CategoryListView,
    ProductInstitutionAssociationCreateView,
    ProductListCreateView,
    ProductRetrieveView,
)

urlpatterns: List = [
    path("", ProductListCreateView.as_view(), name="product_list_create_view"),
    path("<int:pk>", ProductRetrieveView.as_view(), name="product_retrieve_view"),
    path(
        "institution-associated",
        ProductInstitutionAssociationCreateView.as_view(),
        name="product_institution_associated_create_view",
    ),
    path("category/", CategoryListView.as_view(), name="category_list_view"),
]
