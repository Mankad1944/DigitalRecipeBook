# from django.db import models

# # Create your models here.
# class Friend(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.IntegerField()
#     password1=models.CharField(max_length=15)
#     password2=models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.name}"

from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)  # First name
    surname = models.CharField(max_length=100, blank=True, null=True)  # Last name
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password1 = models.CharField(verbose_name="Password",max_length=128)  # store raw password
    # password2 = models.CharField(verbose_name="Confirm Password",max_length=128)  # confirmation password
    # otp = models.CharField(max_length=6, blank=True, null=True)  # for OTP verification
    image = models.ImageField(upload_to="friends/",default="friends/default1.jpg",blank=True,null=True)
    def __str__(self):
        return f"{self.name} {self.surname or ''}".strip()