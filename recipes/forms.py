from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields=['sweetname','category','origin','festival','servings','preptime','cooktime','ingredients','mainingredients','instructions','cooking_method','texture']
        fields="__all__"
        exclude = ["friend"]