from django.contrib import admin

from cook_book.models import Product, Recipe, ProductRecipe


class ProductRecipeInline(admin.TabularInline):
    model = ProductRecipe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'used')
    fields = ('id', 'name')
    readonly_fields = ('id', 'used')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_products')
    exclude = ('products',)
    inlines = [ProductRecipeInline]

    @admin.display(description='products')
    def get_products(self, obj):
        return [product for product in obj.products.all()]
