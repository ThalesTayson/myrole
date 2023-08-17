from django.urls import path
from administradores.controllers.Templates import home

urlpatterns = [
    path('permissoes', home, name='login'),
]