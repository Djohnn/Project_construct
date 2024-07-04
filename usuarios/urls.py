from . import views
from django.urls import path

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name='sair')
]
