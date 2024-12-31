from django.contrib import admin
from .models import Drink # . refers to the same directory

admin.site.register(Drink)
