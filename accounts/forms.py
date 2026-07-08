# from django import forms
# from .models import Friend


# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ['name','email','phone','password1','password2']   # include fields you want in form

# class LoginForm(forms.Form):
#     email=forms.EmailField(label="Email")
#     password=forms.CharField(widget=forms.PasswordInput,label="Password")

from django import forms
from django.core.exceptions import ValidationError
from .models import Friend
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe

class PlainClearableFileInput(ClearableFileInput):
    initial_text = ""          # hide 'Currently'
    input_text = ""            # hide 'Change'
    clear_checkbox_label = ""  # hide 'Clear'

    def format_value(self, value):
        # Don't display the current file name
        return ""
    
    def render(self, name, value, attrs=None, renderer=None):
        # Call the parent render method to get the normal input HTML
        input_html = super().render(name, value, attrs, renderer)
        # Remove the clear checkbox by stripping it from the HTML
        # ClearableFileInput usually outputs a span + input + checkbox
        # We'll just keep the input
        if 'type="checkbox"' in input_html:
            input_html = input_html.split('<input type="checkbox"')[0] + input_html.split('</label>')[-1]
        return mark_safe(input_html)


# 🔹 Registration Form (with password1, password2)
class FriendForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Friend
        fields = ["name", "surname", "email", "phone", "password1", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "surname": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "image": PlainClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # password1 = cleaned_data.get("password1")

        # ✅ Auto split name/surname if needed
        full_name = cleaned_data.get("name", "")
        if full_name and " " in full_name and not cleaned_data.get("surname"):
            parts = full_name.strip().split(" ", 1)
            cleaned_data["name"] = parts[0]
            cleaned_data["surname"] = parts[1] if len(parts) > 1 else ""

        return cleaned_data


# 🔹 Edit Profile Form (without password fields)


class FriendEditForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput, required=False, label="New Password"
    )
    remove_image = forms.BooleanField(required=False, label="Remove profile image")

    class Meta:
        model = Friend
        fields = ["name", "surname", "email", "phone", "image"]  # only real model fields
        widgets = {
            "image": PlainClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # password = cleaned_data.get("password")

        return cleaned_data

    def save(self, commit=True):
        friend = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            friend.password1 = password  # save plain text, if no hashing
        if commit:
            friend.save()
        return friend



# 🔹 Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )