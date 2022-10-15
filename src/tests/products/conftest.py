from typing import Dict, List

import pytest
from factory.base import FactoryMetaClass


@pytest.fixture
def check_product_list(product_factory: FactoryMetaClass) -> List[Dict]:
    product1 = product_factory()
    product2 = product_factory()
    return [
        {
            "id": product1.pk,
            "title": product1.title,
            "category": {"id": product1.category.pk, "title": product1.category.title},
        },
        {
            "id": product2.pk,
            "title": product2.title,
            "category": {"id": product2.category.pk, "title": product2.category.title},
        },
    ]


@pytest.fixture
def check_product_retrieve(product_factory: FactoryMetaClass) -> Dict:
    product = product_factory()
    return {
        "id": product.pk,
        "title": product.title,
        "category": {"id": product.category.pk, "title": product.category.title},
        "institutions": [],
    }


@pytest.fixture
def check_category_list(category_factory: FactoryMetaClass) -> List[Dict]:
    category1 = category_factory()
    category2 = category_factory()
    return [{"id": category1.pk, "title": category1.title}, {"id": category2.pk, "title": category2.title}]
