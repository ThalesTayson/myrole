from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', include('administradores.routes'), name = 'administradores'),
    path('users/', include('users.routes'), name = 'users'),
    path('/', include('app.routes'), name = 'app'),
]
