from django.db import models
from accounts.models import Friend

class Recipe(models.Model):
    sweetname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    festival = models.CharField(max_length=100)
    servings = models.CharField(max_length=100)
    preptime = models.IntegerField()
    cooktime = models.IntegerField()
    ingredients = models.TextField()
    mainingredients = models.CharField(max_length=200)
    instructions = models.TextField()
    cooking_method = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)   # ✅ Added image
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return self.sweetname