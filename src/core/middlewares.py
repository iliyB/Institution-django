from datetime import datetime
from typing import Any

import jwt
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions
from rest_framework.request import Request

from configs import settings
from utils.time import get_current_time


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request) -> Any:
        authorization_header = request.headers.get("Authorization")

        if not authorization_header or authorization_header.split(" ")[0].lower() != "bearer":
            return None
        try:
            access_token = authorization_header.split(" ")[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms="HS256")
        except Exception:
            raise exceptions.AuthenticationFailed({"info": "Invalid token"})
        expire = datetime.strptime(payload["expire"], "%Y-%m-%d %H:%M:%S.%f%z")
        if get_current_time() < expire:
            try:
                user = get_user_model().objects.get(pk=payload["id"])
                user.last_login = get_current_time()
                user.save()
            except Exception:
                raise exceptions.NotFound({"info": "User not found"})
            return user, None
        else:
            raise exceptions.AuthenticationFailed({"info": "Token expire"})
