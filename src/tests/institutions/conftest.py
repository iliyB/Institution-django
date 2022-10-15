from typing import Dict, List, Tuple

import pytest
from factory.base import FactoryMetaClass


@pytest.fixture
def check_institution_list(
    institution_factory: FactoryMetaClass, district_factory: FactoryMetaClass
) -> Tuple[int, List[Dict]]:
    district1 = district_factory()
    district2 = district_factory()
    institution1 = institution_factory(districts=[district1, district2])
    institution2 = institution_factory(districts=[district1])
    return district1.pk, [
        {
            "id": institution1.pk,
            "title": institution1.title,
            "enterprise_network": {
                "id": institution1.enterprise_network.pk,
                "title": institution1.enterprise_network.title,
            },
        },
        {
            "id": institution2.pk,
            "title": institution2.title,
            "enterprise_network": {
                "id": institution2.enterprise_network.pk,
                "title": institution2.enterprise_network.title,
            },
        },
    ]


@pytest.fixture
def check_institution_retrieve(institution_factory: FactoryMetaClass, district_factory: FactoryMetaClass) -> Dict:
    institution = institution_factory(districts=[district_factory(), district_factory()])
    return {
        "id": institution.pk,
        "title": institution.title,
        "description": institution.description,
        "enterprise_network": {"id": institution.enterprise_network.pk, "title": institution.enterprise_network.title},
        "districts": [{"id": district.pk, "title": district.title} for district in institution.districts.all()],
        "products": [],
    }
