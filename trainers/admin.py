from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Trainer
from .models import TrainerFeedback

class TrainerAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'age', 'user', 'featured_image')
    list_filter = ('age',)
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name',)
    fields = ('user', 'first_name', 'last_name', 'age', 'description', 'featured_image')


class TrainerFeedbackAdmin(SummernoteModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('user', 'trainer', 'rating', 'created_at', 'updated_at') 
    list_filter = ('trainer', 'rating')  
    search_fields = ('user__username', 'trainer__first_name', 'trainer__last_name')  

    summernote_fields = ('comment',)

# Register your models here.

admin.site.register(Trainer, TrainerAdmin)
admin.site.register(TrainerFeedback, TrainerFeedbackAdmin)