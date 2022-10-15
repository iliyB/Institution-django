from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedTabularInline

from institutions.models import ProductInstitutionAssociated
from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class ProductInstitutionAssociatedInline(NestedTabularInline):
    """
    Инлайн модель для предприятий, привязанных к товару/услуге
    """

    model = ProductInstitutionAssociated
    extra = 0


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ("id", "title", "category")
    list_select_related = ("category",)
    inlines = (ProductInstitutionAssociatedInline,)
