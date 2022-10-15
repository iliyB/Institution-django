from typing import Dict, List

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestProduct:
    def test_product_list(self, api_client: APIClient, get_auth_token: str, check_product_list: List[Dict]) -> None:
        url = reverse("product_list_create_view")
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json() == check_product_list

    def test_product_retrieve(self, api_client: APIClient, get_auth_token: str, check_product_retrieve: Dict) -> None:
        url = reverse("product_retrieve_view", kwargs={"pk": check_product_retrieve.get("id")})
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json() == check_product_retrieve

    def test_product_create(self, api_client: APIClient, get_auth_token: str, category_id: int) -> None:
        url = reverse("product_list_create_view")
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)

        title = "test product"
        response = api_client.post(url, data={"title": title, "category": category_id})
        assert response.status_code == 201

        response_json = response.json()
        assert response_json.get("title") == title
        assert response_json.get("category") == category_id
        assert type(response_json.get("id")) is int

    def test_category_list(self, api_client: APIClient, get_auth_token: str, check_category_list: List[Dict]) -> None:
        url = reverse("category_list_view")
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.json() == check_category_list

    @pytest.mark.parametrize("price, status_code", [(21.0, 201), (-2.0, 400)])
    def test_institution_associated_create(
        self,
        api_client: APIClient,
        get_auth_token: str,
        product_id: int,
        institution_id: int,
        price: float,
        status_code: int,
    ) -> None:
        url = reverse("product_institution_associated_create_view")
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)

        data = {
            "institution": institution_id,
            "product": product_id,
            "price": price,
        }
        response = api_client.post(url, data=data)
        assert response.status_code == status_code
