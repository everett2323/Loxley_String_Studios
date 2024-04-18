from django.contrib import admin

from UserManagement.models import CustomUser, CustomUserAdmin

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CustomUserAdmin)
