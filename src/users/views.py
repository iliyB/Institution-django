from typing import List

from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsBasicAuth


class UserAuthorizationView(APIView):
    permission_classes = [IsAuthenticated, IsBasicAuth]

    def get(self, request: Request) -> Response:
        """
        Авторизация по basic для получения bearer токена.
        Авторизациф по basic проходит через
        rest_framework.authentication.BasicAuthentication"
        """
        return Response(data={"access_token": request.user.get_access_token})

    def get_permissions(self) -> List[BasePermission]:
        self.permission_classes += [IsBasicAuth]
        return super().get_permissions()
