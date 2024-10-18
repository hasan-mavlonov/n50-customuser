from django.contrib import admin
from .models import CustomUser  # Import your model

# Register your CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')  # Customize fields shown in the list view
    search_fields = ('email', 'first_name', 'last_name')  # Add search functionality
    list_filter = ('is_active',)  # Add filters for easy navigation