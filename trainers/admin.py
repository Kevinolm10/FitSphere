from django.contrib import admin
from .models import Trainer

# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'age', 'user', 'featured_image')

    # Fields to filter by in the admin interface
    list_filter = ('age',)

    # Enable search functionality for these fields
    search_fields = ('first_name', 'last_name')

    # Default ordering in the admin list view
    ordering = ('last_name',)

    # Specify the fields to display in the form view
    fields = ('user', 'first_name', 'last_name', 'age', 'description', 'featured_image')


admin.site.register(Trainer, TrainerAdmin)
