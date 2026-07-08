from django.shortcuts import render
from accounts.models import Friend
from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe

# Welcome page
def welcome(request):
    user_id = request.session.get("user_id")
    friend = None
    if user_id:
        friend = get_object_or_404(Friend, id=user_id)
    return render(request, 'core/welcome.html', {"friend": friend})

# Home page with filters
def home(request):
    filter_by = request.GET.get("filter-switch")  # which field to filter (name/state/product)
    search_query = request.GET.get("q")           # the search text

    recipes = Recipe.objects.all()

    if search_query:  # only filter if user typed something
        if filter_by == "name":
            recipes = recipes.filter(sweetname__icontains=search_query)
        elif filter_by == "state":
            recipes = recipes.filter(origin__icontains=search_query)
        elif filter_by == "product":
            recipes = recipes.filter(category__icontains=search_query)

    context = {
        "recipes": recipes,
        "filter_by": filter_by,
        "search_query": search_query,
    }

    return render(request, "core/home.html", {"recipes": recipes})
