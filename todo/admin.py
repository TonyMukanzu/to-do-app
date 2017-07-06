from django.contrib import admin

# Register your models here.
from .models import Category, Tasks

admin.site.register(Category)
admin.site.register(Tasks)
