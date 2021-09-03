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



        processed_drinks = [
            {'name':d.name,
             'picture_url':self.get_picture_url(d),
             'in_stock':all([i.in_stock for i in d.ingredients.all()]),
             'ingredients': self.get_ingredients(d)
            } for d in drinks]
        return processed_drinks


    def get_ingredients(self, drink):
        return [i.name for i in drink.ingredients.all()]

    def get_picture_url(self, drink):
        if drink.picture:
            return drink.picture.url
        else:
            return ""
