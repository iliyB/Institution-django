from django.views import View
from rest_framework import permissions
from rest_framework.request import Request


class IsBasicAuth(permissions.BasePermission):
    """
    Проверяет, что авторизация происходит по Basic
    """

    def has_permission(self, request: Request, _: View) -> bool:
        try:
            auth_header = request.headers.get("Authorization").split()
            return auth_header[0].lower() == "basic"
        except:
            return False
