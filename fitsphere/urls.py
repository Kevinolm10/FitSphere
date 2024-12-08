from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('pt/', include('pt.urls')),  # pt app URLs
    path("accounts/", include("allauth.urls")),
    path('trainers/', include('trainers.urls')),
    path('about/', include('about.urls')),
    path('', include('pt.urls')),  # This will use the pt app for the homepage
]