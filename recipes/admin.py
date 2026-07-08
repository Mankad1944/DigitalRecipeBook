from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id','image','sweetname','category','origin','festival','servings',
        'preptime','cooktime','mainingredients','cooking_method',
        'texture','friend','created_at'
    )
    search_fields = ('sweetname',)
    list_filter=('origin','festival',)