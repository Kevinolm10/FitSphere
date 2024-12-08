from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Trainer
from .models import TrainerFeedback

# Trainer Admin
class TrainerAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = (
        'first_name', 
        'last_name', 
        'age', 
        'user', 
        'featured_image', 
        'created_at'
    )

    # Filter options
    list_filter = ('age',)

    # Search fields
    search_fields = ('first_name', 'last_name')

    # Ordering in the admin
    ordering = ('last_name',)

    # Fields to display in the detail view form
    fields = (
        'user', 
        'first_name', 
        'last_name', 
        'age', 
        'description', 
        'featured_image'
    )

    # Read-only fields in the form (you can add created_at if needed)
    readonly_fields = ('created_at',)


# TrainerFeedback Admin with Summernote
class TrainerFeedbackAdmin(SummernoteModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('user', 'trainer', 'rating', 'created_at', 'updated_at')

    # Filter options
    list_filter = ('trainer', 'rating')

    # Search fields
    search_fields = ('user__username', 'trainer__first_name', 'trainer__last_name')

    # Summernote for the comment field (rich text editor)
    summernote_fields = ('comment',)

    # Read-only fields for timestamps
    readonly_fields = ('created_at', 'updated_at')

    # Ordering feedback by created_at
    ordering = ('-created_at',)

# Register models
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(TrainerFeedback, TrainerFeedbackAdmin)