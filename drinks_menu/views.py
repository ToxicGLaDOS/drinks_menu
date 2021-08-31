from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Ingredient, Drink

def drink(request, drink_name):
    return HttpResponse(f"Requested drink: {drink_name}")

class IndexView(generic.ListView):
    template_name = "drinks_menu/index.html"
    context_object_name = "drinks_list"

    def get_queryset(self):
        drinks = Drink.objects.order_by('name')

        processed_drinks = [{'drink':d, 'in_stock':all([i.in_stock for i in d.ingredients.all()])} for d in drinks]
        return processed_drinks

