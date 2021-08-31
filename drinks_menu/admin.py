from django.contrib import admin
from .models import Ingredient, Drink, MeasuredIngredient


class MeasuredIngredientInline(admin.TabularInline):
    model = MeasuredIngredient
    extra = 0

class DrinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ("Image", {'fields': ['picture']})
    ]
    inlines = [MeasuredIngredientInline]



admin.site.register(Ingredient)
admin.site.register(Drink, DrinkAdmin)
