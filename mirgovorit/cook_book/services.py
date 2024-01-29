from django.db.models import F, Q, QuerySet
from django.shortcuts import get_object_or_404

from cook_book.models import Recipe, Product, ProductRecipe


class CookBookServices:

    MIN_WEIGHT = 10

    @staticmethod
    def add_product_to_recipe(recipe_id: int, product_id: int, weight: int) -> None:
        """Бизнес логика добавления продукта в рецепт"""

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        obj, _ = ProductRecipe.objects.get_or_create(product=product, recipe=recipe)
        obj.weight = weight
        obj.save()

    @staticmethod
    def cook_recipe(recipe_id: int) -> None:
        """Бизнес логика готовки рецепта"""

        recipe = get_object_or_404(Recipe, pk=recipe_id)

        product_ids = recipe.products.values_list('id', flat=True)
        Product.objects.filter(pk__in=product_ids).update(used=F('used') + 1)

    @staticmethod
    def show_recipes_without_product(product_id: int) -> tuple[Product, QuerySet]:
        """Бизнес логика отображения рецептов без наличия в нем некоего продукта"""

        product = get_object_or_404(Product, pk=product_id)
        return product, Recipe.objects\
                              .exclude(Q(products=product), ~Q(productrecipe__weight__lt=CookBookServices.MIN_WEIGHT))
