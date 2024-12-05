from django.urls import path  
from . import views
urlpatterns = [
    path('', views.trainers, name='trainers'),  # URL pattern for the trainers page
    path('trainer/<int:trainer_id>/', views.trainer_profile, name='trainer_profile'),
    path('trainer/<int:trainer_id>/feedback/', views.submit_feedback, name='submit_feedback'),
]