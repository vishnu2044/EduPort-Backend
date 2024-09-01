from django.contrib import admin
from .models.country import Country
from .models.state import State
from .models.qualification import Qualification

@admin.register(Country)
class CountryDisplay(admin.ModelAdmin):
    list_display = (
        'id', 
        'name',
    )

    search_fields = (
        'id', 
        'name',
    )
    list_filter = (
        'name',
    )

@admin.register(State)
class StateDisplay(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'country',
        )

    search_fields = (
        'id', 
        'name', 
        'country__name',
        'name', 
        'country',
    )

    list_filter = (
        'country',
    )

@admin.register(Qualification)
class QualificationDisplay(admin.ModelAdmin):
    list_display = (
        'id', 
        'qualification',
    )
    search_fields = (
        'id', 
        'qualification',
    )
    # list_filter = (
    #     'qualification',
    # )