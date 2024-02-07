from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='index'),
    # Add other URL patterns for additional views if needed
]
