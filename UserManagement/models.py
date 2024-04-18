from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    class InstrumentType(models.TextChoices):
        cello = "Cello", "cello"
        violin = "Violin", "violin"
        bass = "Bass", "bass"
        viola = "Viola", "viola"

    age = models.IntegerField(default=0)
    instrument = models.CharField(max_length=20, choices=InstrumentType.choices, default="Pleas choose your instrument")
    experience = models.IntegerField(default=0)

 class CustomUserAdmin(UserAdmin):
     form = CustomUserChangeForm #TODO: ERROR
     addForm = CustomUserCreationForm #TODO: ERROR
     model = CustomUser
     fieldsets = UserAdmin.fieldsets + ((None, {"fields":"age,instrument,experience"}),)
     add_fieldsets = UserAdmin.add_fieldsets((None, {"fields":"age,instrument,experience"}),)


