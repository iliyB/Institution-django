from typing import Type

from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer

from institutions.models import ProductInstitutionAssociated
from products.models import Category, Product
from products.serializers import (
    CategorySerializer,
    ProductCreateSerializer,
    ProductInstitutionAssociatedCreateSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
)


class CategoryListView(ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(ListCreateAPIView):
    model = Product
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductListSerializer

    def get_serializer_class(self) -> Type[ModelSerializer]:
        if self.request.method == "GET":
            return ProductListSerializer
        elif self.request.method == "POST":
            return ProductCreateSerializer

        return self.serializer_class


class ProductRetrieveView(RetrieveAPIView):
    model = Product
    queryset = Product.objects.select_related("category").prefetch_related("institutions").all()
    serializer_class = ProductRetrieveSerializer


class ProductInstitutionAssociationCreateView(CreateAPIView):
    model = ProductInstitutionAssociated
    serializer_class = ProductInstitutionAssociatedCreateSerializer
