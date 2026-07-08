# from django.shortcuts import render, redirect
# from .forms import RecipeForm
# from accounts.models import Friend

# def add_recipe(request):
#     if 'user_id' not in request.session:
#         return redirect('login')

#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             recipe = form.save(commit=False)

#             friend = Friend.objects.get(id=request.session['user_id'])
#             recipe.friend = friend
#             recipe.save()

#             return redirect("recipe_add")
#     else:
#         form = RecipeForm()

#     return render(request, 'recipes/recipe_add.html', {"form": form})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Recipe
# from .forms import RecipeForm
# from accounts.models import Friend

# # ✅ Recipe List (Only User’s Recipes)
# def recipe_list(request):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipes = Recipe.objects.filter(friend=friend)

#     return render(request, "recipes/recipe_list.html", {"recipes": recipes, "friend": friend})

# # ✅ Create Recipe
# def recipe_create(request):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)

#     if request.method == "POST":
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.friend = friend   # link recipe to logged-in user
#             recipe.save()
#             return redirect("recipe_list")
#     else:
#         form = RecipeForm()

#     return render(request, "recipes/recipe_form.html", {"form": form, "action": "Create"})

# # ✅ Update Recipe
# def recipe_update(request, pk):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipe = get_object_or_404(Recipe, pk=pk, friend=friend)

#     if request.method == "POST":
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect("recipe_list")
#     else:
#         form = RecipeForm(instance=recipe)

#     return render(request, "recipes/recipe_form.html", {"form": form, "action": "Update"})

# # ✅ Delete Recipe
# def recipe_delete(request, pk):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipe = get_object_or_404(Recipe, pk=pk, friend=friend)

#     if request.method == "POST":
#         recipe.delete()
#         return redirect("recipe_list")

#     return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Recipe
# from .forms import RecipeForm
# from accounts.models import Friend

# # ✅ Recipe List (Only User’s Recipes)
# def recipe_list(request):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipes = Recipe.objects.filter(friend=friend)

#     return render(request, "recipes/recipe_list.html", {"recipes": recipes, "friend": friend})


# # ✅ Create Recipe
# def recipe_create(request):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)

#     if request.method == "POST":
#         form = RecipeForm(request.POST, request.FILES)  # ✅ request.FILES added
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.friend = friend
#             recipe.save()
#             return redirect("recipe_list")
#     else:
#         form = RecipeForm()

#     return render(request, "recipes/recipe_form.html", {"form": form, "action": "Add", "friend": friend})


# # ✅ Update Recipe
# def recipe_update(request, pk):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipe = get_object_or_404(Recipe, pk=pk, friend=friend)

#     if request.method == "POST":
#         form = RecipeForm(request.POST, request.FILES, instance=recipe)  # ✅ request.FILES added
#         if form.is_valid():
#             form.save()
#             return redirect("recipe_list")
#     else:
#         form = RecipeForm(instance=recipe)

#     return render(request, "recipes/recipe_form.html", {"form": form, "action": "Update", "friend": friend})


# # ✅ Delete Recipe
# def recipe_delete(request, pk):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     friend = Friend.objects.get(id=user_id)
#     recipe = get_object_or_404(Recipe, pk=pk, friend=friend)

#     if request.method == "POST":
#         recipe.delete()
#         return redirect("recipe_list")

#     return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})

# # def recipe_detail(request, pk):
# #     user_id = request.session.get("user_id")
# #     if not user_id:   # ✅ check session, not Django auth
# #         return redirect("login")

# #     recipe = get_object_or_404(Recipe, pk=pk)
# #     return render(request, "recipes/recipe_detail.html", {"recipe": recipe})

# def recipe_detail(request, pk):
#     user_id = request.session.get("user_id")
#     if not user_id:
#         return redirect("login")

#     # ✅ Get recipe
#     recipe = get_object_or_404(Recipe, pk=pk)

#     # ✅ Get related friend (assuming Recipe has a ForeignKey to Friend)
#     friend = recipe.friend  

#     # ✅ Process ingredients into structured rows
#     ingredients_list = []
#     for line in recipe.ingredients.splitlines():
#         parts = line.split()
#         if len(parts) >= 3:
#             name = parts[0].capitalize()
#             quantity = parts[1]
#             unit = " ".join(parts[2:])
#         elif len(parts) == 2:
#             name, quantity = parts[0], parts[1]
#             unit = ""
#         else:
#             name, quantity, unit = line, "", ""
#         ingredients_list.append({
#             "name": name,
#             "quantity": quantity,
#             "unit": unit
#         })

#     return render(request, "recipes/recipe_detail.html", {
#         "recipe": recipe,
#         "friend": friend,   # ✅ now friend is defined
#         "ingredients_list": ingredients_list,
#     })


# recipes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Recipe
from .forms import RecipeForm
from accounts.models import Friend
from .serializers import RecipeSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# ✅ Class-Based View for HTML recipe list
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("user_id"):
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.request.session.get("user_id")
        friend = Friend.objects.get(id=user_id)
        return Recipe.objects.filter(friend=friend).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get("user_id")
        context['friend'] = Friend.objects.get(id=user_id)
        return context


# ✅ DRF API ViewSet
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]  # You can change to IsAuthenticated later

    def perform_create(self, serializer):
        # If using session-based login
        user_id = self.request.session.get("user_id")
        if user_id:
            friend = Friend.objects.get(id=user_id)
            serializer.save(friend=friend)
        else:
            # If friend_id is passed from API request
            friend_id = self.request.data.get("friend_id")
            if friend_id:
                friend = Friend.objects.get(id=friend_id)
                serializer.save(friend=friend)
            else:
                raise ValueError("Friend must be provided.")


# ✅ Function-based views (HTML)
def recipe_create(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    friend = Friend.objects.get(id=user_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.friend = friend
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form, "action": "Add", "friend": friend})


def recipe_update(request, pk):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    friend = Friend.objects.get(id=user_id)
    recipe = get_object_or_404(Recipe, pk=pk, friend=friend)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/recipe_form.html", {"form": form, "action": "Update", "friend": friend})


def recipe_delete(request, pk):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    friend = Friend.objects.get(id=user_id)
    recipe = get_object_or_404(Recipe, pk=pk, friend=friend)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})


def recipe_detail(request, pk):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    friend = Friend.objects.get(id=user_id)
    recipe = get_object_or_404(Recipe, pk=pk)

    ingredients_list = []
    if recipe.ingredients:
        for line in recipe.ingredients.splitlines():
            parts = line.split()
            if len(parts) >= 3:
                name = " ".join(parts[:-2]).capitalize()
                quantity = parts[-2]
                unit = parts[-1]
            elif len(parts) == 2:
                name, quantity = parts[0].capitalize(), parts[1]
                unit = ""
            else:
                name, quantity, unit = line, "", ""
            ingredients_list.append({"name": name, "quantity": quantity, "unit": unit})

    return render(request, "recipes/recipe_detail.html", {
        "recipe": recipe,
        "friend": friend,
        "ingredients_list": ingredients_list,
    })
