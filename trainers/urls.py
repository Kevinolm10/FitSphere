from django.urls import path
from . import views

app_name = 'trainers'

urlpatterns = [
    path('', views.trainers, name='trainers'),
    path('trainer/<int:trainer_id>/',
    views.trainer_profile, name='trainer_profile'),
    path('feedback/delete/<int:id>/',
    views.delete_feedback, name='delete_feedback'),
    path('feedback/edit/<int:feedback_id>/',
    views.edit_feedback, name='edit_feedback'),
    path('trainer/<int:trainer_id>/feedback/',
    views.submit_feedback, name='submit_feedback'),
]