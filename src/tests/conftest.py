from typing import Tuple

import pytest
from django.contrib.auth import get_user_model
from factory.base import FactoryMetaClass
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import CategoryFactory, DistrictFactory, InstitutionFactory, ProductFactory

register(CategoryFactory)
register(ProductFactory)
register(DistrictFactory)
register(InstitutionFactory)


@pytest.fixture(scope="session")
def user_credentials() -> Tuple[str, str]:
    """
    :return: Tuple[username, password]
    """
    return "test_user", "qesd2312SDS"


@pytest.fixture
def get_auth_token(user_credentials: Tuple[str, str]) -> str:
    user = get_user_model().objects.create(username=user_credentials[0], password=user_credentials[1])
    return user.get_access_token


@pytest.fixture(scope="session", autouse=True)
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def product_id(product_factory: FactoryMetaClass) -> int:
    product = product_factory()
    return product.pk


@pytest.fixture
def category_id(category_factory: FactoryMetaClass) -> int:
    category = category_factory()
    return category.pk


@pytest.fixture
def institution_id(institution_factory: FactoryMetaClass, district_factory: FactoryMetaClass) -> int:
    institution = institution_factory(districts=[district_factory()])
    return institution.pk
