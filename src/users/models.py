from datetime import timedelta

import jwt
from django.contrib.auth.models import AbstractUser

from configs import settings
from utils.time import get_current_time


class User(AbstractUser):
    """
    МОдель пользователя
    """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return str(self.email)

    @property
    def get_access_token(self) -> str:
        return self._generate_jwt_token()

    def _generate_jwt_token(self) -> str:
        token = jwt.encode(
            {"id": self.pk, "expire": str(get_current_time() + timedelta(days=60))},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
