from django.contrib import admin
from .models import   UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'
    
class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, UserAdmin)