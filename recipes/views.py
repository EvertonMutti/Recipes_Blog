from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from django.http import HttpResponse
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    #recipes = get_list_or_404( Recipe.objects.filter(is_published=True,).order_by('-id'))
    return render(request,'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_detail_page': False,
    })

def category(request, category_id):
    #recipes = Recipe.objects.filter(is_published=True,category__id=category_id,).order_by('-id')
    
    recipes = get_list_or_404( Recipe.objects.filter(is_published=True,category__id=category_id,).order_by('-id'))

    return render(request,'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    })

def recipe(request, recipe_id):
    #recipe = Recipe.objects.filter(is_published = True, pk = recipe_id).order_by('-id').first()

    recipe = get_object_or_404(
        Recipe,
        is_published = True,
        pk = recipe_id)
    
    return render(request,'recipes/pages/recipe-view.html', context={
       'recipe': recipe,
        'is_detail_page': True,
    })
# Create your views here.
