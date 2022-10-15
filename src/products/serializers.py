from rest_framework import serializers

from institutions.models import ProductInstitutionAssociated
from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductInstitutionAssociatedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInstitutionAssociated
        exclude = ()


class ProductInstitutionAssociatedSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вывода предприятий товара/услуги через связанную модель
    """

    id = serializers.ReadOnlyField(source="institution.id")
    title = serializers.ReadOnlyField(source="institution.title")

    class Meta:
        model = ProductInstitutionAssociated
        fields = ("id", "title", "price")


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "category")


class ProductListSerializer(ProductCreateSerializer):
    category = CategorySerializer(read_only=True)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    institutions = ProductInstitutionAssociatedSerializer(many=True, source="productinstitutionassociated_set")

    class Meta:
        model = Product
        exclude = ()
