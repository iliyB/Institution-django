from typing import Dict, List

import factory.django

from institutions.models import District, EnterpriseNetwork, Institution, ProductInstitutionAssociated
from products.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(lambda n: f"category{n}")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"product{n}")
    category = factory.SubFactory(CategoryFactory)


class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District

    title = factory.Sequence(lambda n: f"district{n}")


class EnterpriseNetworkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EnterpriseNetwork

    title = factory.Sequence(lambda n: f"enterprice{n}")


class InstitutionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Institution

    title = factory.Sequence(lambda n: f"institution{n}")
    enterprise_network = factory.SubFactory(EnterpriseNetworkFactory)

    @factory.post_generation
    def districts(self, create: bool, extracted: List[District], **kwargs: Dict) -> None:
        if not create:
            return

        if extracted:
            for district in extracted:
                self.districts.add(district)
