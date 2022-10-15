from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedTabularInline

from institutions.models import District, EnterpriseNetwork, Institution, ProductInstitutionAssociated


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(EnterpriseNetwork)
class EnterpriseNetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class InstitutionProductAssociatedInline(NestedTabularInline):
    """
    Инлайн модель для вывода товар/услуг, привязанных к предприятию
    """

    model = ProductInstitutionAssociated
    extra = 0


@admin.register(Institution)
class InstitutionNetworkAdmin(NestedModelAdmin):
    list_display = ("id", "title", "enterprise_network")
    list_select_related = ("enterprise_network",)
    inlines = (InstitutionProductAssociatedInline,)
