from rest_framework import serializers

from institutions.models import District, EnterpriseNetwork, Institution, ProductInstitutionAssociated


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        exclude = ()


class EnterpriseNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseNetwork
        exclude = ()


class InstitutionProductAssociatedSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вывода товаров и услуг предприятия через связанную модель
    """

    id = serializers.ReadOnlyField(source="product.id")
    title = serializers.ReadOnlyField(source="product.title")

    class Meta:
        model = ProductInstitutionAssociated
        fields = ("id", "title", "price")


class InstitutionListSerializer(serializers.ModelSerializer):
    enterprise_network = EnterpriseNetworkSerializer(read_only=True)

    class Meta:
        model = Institution
        fields = ("id", "title", "enterprise_network")


class InstitutionRetrieveSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)
    enterprise_network = EnterpriseNetworkSerializer(read_only=True)
    products = InstitutionProductAssociatedSerializer(many=True, source="productinstitutionassociated_set")

    class Meta:
        model = Institution
        exclude = ()
