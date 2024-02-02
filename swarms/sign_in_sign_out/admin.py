from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "user"]
    list_filter = ["county"]


admin.site.unregister(User)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """_summary_
sets the email address as the editable link in Admin (Unregister user is important here)
UserAdmin keeps all the standard items in the Change User screen
    """

    list_display = ['email', 'first_name', 'last_name',
                    'is_staff', 'is_superuser', "username"]
    search_fields = ["email"]
