# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .forms import FriendForm,LoginForm
# from .models import Friend


# # Create your views here.

# def register(request):
#     if request.method == "POST":
#         form = FriendForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('per_register')   # redirect after saving
#         return render(request, 'accounts/register.html')
#     else:
#         form = FriendForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def success(request):
#     return render(request,'accounts/success.html')

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             try:
#                 user = Friend.objects.get(email=email, password1=password)
#                 request.session['user_id'] = user.id
#                 request.session['user_name'] = user.name
#                 return redirect('home')   # redirect to dashboard/home
#             except Friend.DoesNotExist:
#                 messages.error(request, "Invalid email or password")
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})

# def logout(request):
#     request.session.flush()
#     messages.info(request, "You have been logged out.")
#     return redirect('login')


# accounts/views.py

import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Friend
from .forms import FriendForm, LoginForm, FriendEditForm

# 🔹 Register with OTP Verification
def register(request):
    if request.method == "POST":
        step = request.POST.get("step")

        # STEP 1: Register User (before OTP)
        if step == "1":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            password_plain = request.POST.get("password1")

            otp = str(random.randint(100000, 999999))
            print(f"Generated OTP: {otp}")

            # Temporarily save user data + otp in session
            request.session["temp_user"] = {
                "name": name, "surname": surname, "phone": phone,
                "email": email, "password": password_plain, # Storing plain password
            }
            request.session["otp"] = otp
            return render(request, "accounts/register.html", {"show_otp_box": True})

        # STEP 2: Verify OTP
        elif step == "2":
            entered_otp = request.POST.get("otp")
            if entered_otp == request.session.get("otp"):
                user_data = request.session.get("temp_user")

                # Save user in DB with the plain password
                user = Friend.objects.create(
                    name=user_data["name"], surname=user_data["surname"],
                    phone=user_data["phone"], email=user_data["email"],
                    password=user_data["password"] # Saving plain password
                )

                # Clear OTP data
                del request.session["otp"]
                del request.session["temp_user"]

                messages.success(request, "Registration successful! Please log in.")
                return redirect("login")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "accounts/register.html", {"show_otp_box": True})

    return render(request, "accounts/register.html")


# 🔹 Login View (Reverted to Plain Text)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                # Reverted to insecure plain text password check
                user = Friend.objects.get(email=email, password1=password)

                # Reverted to manual session management
                request.session['user_id'] = user.id
                request.session['user_name'] = f"{user.name} {user.surname or ''}".strip()
                request.session.set_expiry(3600) # 1 hour expiry

                return redirect('welcome')
            except Friend.DoesNotExist:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# 🔹 Logout View (Reverted to Manual Session Flush)
def logout(request):
    # Reverted to flushing the entire session
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect('login')


# 🔹 Profile Page (Reverted to Manual Session Check)
def friend_profile(request):
    user_id = request.session.get("user_id")
    if not user_id:
        messages.warning(request, "Your session has expired. Please log in again.")
        return redirect("login")

    friend = get_object_or_404(Friend, id=user_id)
    return render(request, "accounts/friend_profile.html", {"friend": friend})


# 🔹 Edit Friend Profile (Reverted to Manual Session Check)
def edit_friend(request, pk):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    
    # Ensure users can only edit their own profile
    if user_id != pk:
        messages.error(request, "You are not authorized to edit this profile.")
        return redirect('friend_profile')
        
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == "POST":
        form = FriendEditForm(request.POST, request.FILES, instance=friend)
        if form.is_valid():
            instance = form.save(commit=False)
            if form.cleaned_data.get("remove_image") and not request.FILES.get("image"):
                if instance.image:
                    instance.image.delete(save=False)
                instance.image = "images/default1.jpg"
            instance.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("friend_profile")
    else:
        form = FriendEditForm(instance=friend)
    return render(request, "accounts/friend_edit.html", {"form": form, "friend": friend})


# 🔹 Success Page (No changes needed)
def success(request):
    return render(request, 'accounts/success.html')