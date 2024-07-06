from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from .models import Users


class ProfileInline(admin.StackedInline):
    model = Users
    fields = ['middle_name', 'initial_password_changed_at', 'email']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


# admin.site.register(Permission)
admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.register(User, ProfileAdmin)
