from typing import List

from django.urls import path

from users.views import UserAuthorizationView

urlpatterns: List = [path("authorization/", UserAuthorizationView.as_view(), name="authorization_view")]
