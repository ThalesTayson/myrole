from django.urls import path
from users.controllers.Templates import entrar, sair

urlpatterns = [
    path('accounts/auth/login', entrar, name='login'),
    path('accounts/auth/logout', sair, name='logout'),
]