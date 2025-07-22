from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    
    path('base_login', views.base_login, name='base_login'),

    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('home_vendedor', views.home_vendedor, name='home_vendedor'),
    # path('home', views.home, name='home'),
    #path('actualizarProducto', views.actualizarProducto, name='actualizarProducto'),
    path('actualizarProducto',
         views.actualizarProducto,
         name='actualizarProducto',
    ),
    path('anadirProducto', views.addProducto, name='addProducto')
]