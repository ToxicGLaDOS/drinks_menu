from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Volume

class Glassware(models.Model):
    name = models.CharField(max_length=200)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    in_stock = models.BooleanField()
    is_liquor = models.BooleanField()

    def __str__(self):
        return self.name

class Drink(models.Model):
    ingredients = models.ManyToManyField('Ingredient', through='MeasuredIngredient')
    name = models.CharField(max_length=200)
    # Uploads to MEDIA_ROOT/drink_images/
    picture = models.ImageField(null=True, blank=True, upload_to="drink_images/")
    directions = models.TextField()
    glass = models.ForeignKey(Glassware, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class MeasuredIngredient(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    volume = MeasurementField(measurement=Volume, unit_choices=(("us_oz","oz"),))

    def __str__(self):
        return f"{self.volume.us_oz}oz {str(self.ingredient)}"
