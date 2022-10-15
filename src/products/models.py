from django.db import models


class Category(models.Model):
    """
    Модель категории товара/услуги
    """

    title = models.CharField("Название", max_length=64)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return str(self.title)


class Product(models.Model):
    """
    МОдель товара/услуги
    """

    title = models.CharField("Название", max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")

    class Meta:
        verbose_name = "Продукт/услуга"
        verbose_name_plural = "Продукты и услуги"

    def __str__(self) -> str:
        return str(self.title)
