from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="per_register"),
    path("success/", views.success, name="per_success"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("edit_friend/<int:pk>/", views.edit_friend, name="edit_friend"),
    path("friend_profile/", views.friend_profile, name="friend_profile"),
]