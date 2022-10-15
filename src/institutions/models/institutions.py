from django.db import models

from products.models import Product


class District(models.Model):
    """
    Модель района
    """

    title = models.CharField("Название", max_length=64)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self) -> str:
        return str(self.title)


class EnterpriseNetwork(models.Model):
    """
    Модель сети предприятий
    """

    title = models.CharField("Название", max_length=64)

    class Meta:
        verbose_name = "Сеть предприятий"
        verbose_name_plural = "Сети предприятий"

    def __str__(self) -> str:
        return str(self.title)


class Institution(models.Model):
    """
    Модель предприятия
    """

    title = models.CharField("Название", max_length=64)
    description = models.CharField("Описание", max_length=1024)

    districts = models.ManyToManyField(District, related_name="institutions", verbose_name="Районы")
    enterprise_network = models.ForeignKey(
        EnterpriseNetwork,
        on_delete=models.SET_NULL,
        null=True,
        related_name="institutions",
        verbose_name="Сеть предприятий",
    )
    products = models.ManyToManyField(
        Product, through="ProductInstitutionAssociated", related_name="institutions", verbose_name="Товары и услуги"
    )

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self) -> str:
        return str(self.title)
