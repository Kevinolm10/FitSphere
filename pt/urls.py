from django.urls import path
from . import views

urlpatterns = [
    path('', views.pt, name='index'),  # Home page for the pt app (renders index.html)
]