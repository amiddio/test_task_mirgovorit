from django.urls import path

from cook_book.views import AddProductToRecipe, CookRecipe, ShowRecipesWithoutProduct

app_name = 'cook_book'

urlpatterns = [
    path(
        'add_product_to_recipe/<int:recipe_id>/<int:product_id>/<str:weight>',
        AddProductToRecipe.as_view(),
        name='add-product-to-receipe'
    ),
    path(
        'cook_recipe/<int:recipe_id>',
        CookRecipe.as_view(),
        name='cook-recipe'
    ),
    path(
        'show_recipes_without_product/<int:product_id>',
        ShowRecipesWithoutProduct.as_view(),
        name='show_recipes_without_product'
    ),
]
