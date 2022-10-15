from typing import Dict, List, Tuple

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestInstitution:
    def test_institution_retrieve(
        self, api_client: APIClient, get_auth_token: str, check_institution_retrieve: Dict
    ) -> None:
        url = reverse("institution_retrieve_view", kwargs={"pk": check_institution_retrieve.get("id")})
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json() == check_institution_retrieve

    # Параметрайз, для проверки игнорирования неправильных квери параметров
    @pytest.mark.parametrize(
        "query_params",
        [
            "",
            "?category=1,str",
            "?category_false=1,2",
            "?min_price=str",
            "?max_price=str",
            "?max_price=str&category=1,str",
        ],
    )
    def test_institution_list_by_true_district_id(
        self,
        api_client: APIClient,
        get_auth_token: str,
        check_institution_list: Tuple[int, List[Dict]],
        query_params: str,
    ) -> None:
        url = reverse("institution_list_view", kwargs={"district_pk": check_institution_list[0]})
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url + query_params)
        assert response.status_code == 200
        assert response.json() == check_institution_list[1]

    def test_institution_list_by_false_district_id(
        self, api_client: APIClient, get_auth_token: str, institution_id: int
    ) -> None:
        url = reverse("institution_list_view", kwargs={"district_pk": 5555555})
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json() == []
