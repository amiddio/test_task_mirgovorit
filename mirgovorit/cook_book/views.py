from django.http import HttpResponse
from django.views import View

from cook_book.services import CookBookServices


class AddProductToRecipe(View):

    def get(self, request, recipe_id: int, product_id: int, weight: str) -> HttpResponse:
        CookBookServices.add_product_to_recipe(recipe_id, product_id, weight)
        return HttpResponse("Successfully added product to recipe")


class CookRecipe(View):

    def get(self, request, recipe_id: int) -> HttpResponse:
        CookBookServices.cook_recipe(recipe_id)
        return HttpResponse("Products of recipe were cooked")


class ShowRecipesWithoutProduct(View):

    def get(self, request, product_id: int) -> HttpResponse:
        recipes = CookBookServices.show_recipes_without_product(product_id)
        print(recipes)
        return HttpResponse()
