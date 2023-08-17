from django.urls import path
from app.controllers.Templates import home

urlpatterns = [
    path('home', home, name='login'),
]