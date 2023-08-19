from django.contrib import admin
from .models import Pets, CustomUser

# Register your models here.

admin.site.register(Pets)
admin.site.register(CustomUser)
