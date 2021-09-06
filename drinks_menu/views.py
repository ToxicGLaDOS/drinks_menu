from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Ingredient, Drink

def drink_view(request, drink_name):
    template_name = "drinks_menu/drink.html"
    drink = Drink.objects.filter(name=drink_name)[0]
    context = get_drink_context(drink)

    return render(request, template_name, context)


def get_drink_context(drink):
        return {'name':drink.name,
                'picture_url': get_picture_url(drink),
                'in_stock': all([i.in_stock for i in drink.ingredients.all()]),
                'ingredients': get_ingredients(drink),
                'directions': drink.directions
                }

def get_measurement(measured_ingredient):
    volume = measured_ingredient.volume.us_oz
    # This removes the .0 in 1.0
    if int(volume) == volume:
        return str(int(volume))
    else:
        return str(volume)

def get_ingredients(drink):
    measured_ingredients = drink.measuredingredient_set.all()
    return [{'name': mi.ingredient.name,
      'measurement': get_measurement(mi)
    } for mi in measured_ingredients.all()]

def get_picture_url(drink):
    if drink.picture:
        return drink.picture.url
    else:
        return ""

class IndexView(generic.ListView):
    template_name = "drinks_menu/drinks.html"
    context_object_name = "drinks_list"

    def get_queryset(self):
        drinks = Drink.objects.order_by('name')
        processed_drinks = [get_drink_context(d) for d in drinks]
        return processed_drinks



