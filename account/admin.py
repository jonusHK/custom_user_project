from django.contrib import admin

# Register your models here.

from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']+=('profile','message')

    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('profile','message')}),
    )
    # from django.utils.translation import gettext, gettext_lazy as _ : 언어에 맞게 번역해줌
admin.site.register(User, UserAdmin)
