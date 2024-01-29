from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from cook_book.services import CookBookServices


class AddProductToRecipe(View):
    """Представление добавления продукта в рецепт"""

    def get(self, request, recipe_id: int, product_id: int, weight: int) -> HttpResponse:
        CookBookServices.add_product_to_recipe(recipe_id, product_id, weight)
        return HttpResponse("Successfully added product to recipe")


class CookRecipe(View):
    """Представление готовки рецепта"""

    def get(self, request, recipe_id: int) -> HttpResponse:
        CookBookServices.cook_recipe(recipe_id)
        return HttpResponse("Products of recipe were cooked")


class ShowRecipesWithoutProduct(View):
    """Представление отображения рецептов без наличия в нем некоего продукта"""

    def get(self, request, product_id: int) -> HttpResponse:
        product, recipes = CookBookServices.show_recipes_without_product(product_id)
        context = {
            'product': product,
            'recipes': recipes,
        }
        return render(request, 'cook_book/show_recipes_without_product.html', context)
