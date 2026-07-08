#views.py

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages


# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome {username}!")
#                 return redirect("home")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid login details.")
#     else:
#         form = AuthenticationForm()
#     return render(request, "accounts/login.html", {"form": form})

# def user_logout(request):
#     logout(request)
#     messages.success(request, "You have been logged out successfully.")
#     return redirect("login")


#forms.py

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# accounts/urls.py

# path("login/", views.user_login, name="login"),
# path("logout/", views.user_logout, name="logout"),