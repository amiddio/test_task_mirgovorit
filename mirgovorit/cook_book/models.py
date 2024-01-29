from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта", unique=True)
    used = models.PositiveIntegerField(verbose_name="Сколько раз использовался", default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название рецепта", unique=True)
    products = models.ManyToManyField(Product, through='ProductRecipe')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProductRecipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(verbose_name="Вес продукта", default=0)

    class Meta:
        unique_together = ('product', 'recipe')

    def __str__(self):
        return f"Recipe: {self.recipe.__str__()}, Product: {self.product.__str__()}, Weight: {self.weight.__str__()}"
