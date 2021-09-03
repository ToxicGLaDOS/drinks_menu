from django.urls import path

from . import views

app_name = "drinks_menu"
urlpatterns = [
    path('drinks/', views.IndexView.as_view(), name='all_drinks'),
    path('drinks/<str:drink_name>', views.drink_view, name='specific_drink'),
]
