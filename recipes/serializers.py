from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    # Show friend name (read-only)
    friend = serializers.StringRelatedField(read_only=True)
    # Allow passing friend_id when creating
    friend_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'image', 'sweetname', 'category', 'origin', 'festival',
            'servings', 'preptime', 'cooktime', 'ingredients', 'mainingredients',
            'instructions', 'cooking_method', 'texture',
            'friend', 'friend_id', 'created_at'
        ]
