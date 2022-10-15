import base64
from typing import Tuple

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAuthorization:
    def test_use_bearer_token(self, api_client: APIClient, get_auth_token: str) -> None:
        url = reverse("authorization_view")
        api_client.credentials(HTTP_AUTHORIZATION="Bearer " + get_auth_token)
        response = api_client.get(url)
        assert response.status_code == 403

    def test_true_use_basic_token(self, api_client: APIClient, user_credentials: Tuple[str, str]) -> None:

        user = get_user_model().objects.create(username=user_credentials[0])
        user.set_password(user_credentials[1])
        user.save()

        url = reverse("authorization_view")
        token = base64.b64encode(bytes(f"{user_credentials[0]}:{user_credentials[1]}", "utf-8"))
        api_client.credentials(HTTP_AUTHORIZATION="Basic " + token.decode("utf-8"))
        response = api_client.get(url)
        assert response.status_code == 200
        assert type(response.json().get("access_token")) is str

    def test_false_use_basic_token(self, api_client: APIClient) -> None:
        url = reverse("authorization_view")
        token = base64.b64encode(bytes("fake_user:fake_password", "utf-8"))
        api_client.credentials(HTTP_AUTHORIZATION="Basic " + token.decode("utf-8"))
        response = api_client.get(url)
        assert response.status_code == 403
