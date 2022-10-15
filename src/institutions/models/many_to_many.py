from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from institutions.models.institutions import Institution
from products.models import Product


class ProductInstitutionAssociated(models.Model):
    """
    Модель связи товара/услуги и предприятия
    """

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name="Предприятие")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар/услуга")
    price = models.DecimalField(
        "Цена", max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["institution", "product"], name="institution_and_product_unique"),
        ]
        verbose_name = "Связь товара/услуги и предприятия"
        verbose_name_plural = "Связи товара/услуги и предприятия"

    def __str__(self) -> str:
        return str(self.pk)
