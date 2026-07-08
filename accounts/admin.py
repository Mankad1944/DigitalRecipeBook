from django.contrib import admin
from .models import Friend

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display=('id','name','email','phone','password1','image')
    search_fields=('id','name')
    list_filter=('name','email')

# Username: Hirak, Email: hk@gmail.com
# Username: Coder, Email: hirak@gmail.com
# Username: hirak, Email: ab@gmail.com
# Username: vanshilmankad, Email: vm@gmail.com