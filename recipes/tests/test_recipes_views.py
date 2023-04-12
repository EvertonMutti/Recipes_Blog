# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category',
                                   kwargs={'category_id': 1000}))
        print(response.content)
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:Home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:Home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:Home'))
        self.assertIn(
            '<h1 class="center">No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='')
