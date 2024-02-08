from django.contrib import admin
from .models import Review

@admin.register(Review)
class CustomUserAdmin(admin.ModelAdmin):
    pass