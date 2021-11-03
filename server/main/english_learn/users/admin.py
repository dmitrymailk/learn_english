from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from users.models import UserMeta


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserMeta)
