"""
website urls
"""

from django.urls import path 
from .views import index,contact

app_name="website"

urlpatterns = [
    path('', index,name="index"),
    path('contact/', contact,name="contact"),
]
