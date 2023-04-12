from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('Home/', views.home, name="Home"),
    path('recipes/category/<category_id>/', views.category, name="category"),
    path('recipes/<recipe_id>/', views.recipe, name="recipe"),
    
]