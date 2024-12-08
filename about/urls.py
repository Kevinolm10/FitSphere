from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),  # This creates a URL pattern for '/about/'
]