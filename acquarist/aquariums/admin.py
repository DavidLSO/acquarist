from django.contrib import admin

from acquarist.aquariums.models import EquipamentTypes, TestTypes


@admin.register(EquipamentTypes)
class EquipamentTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TestTypes)
class TestTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    search_fields = ('name',)
