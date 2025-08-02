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
    
    path('anadirProducto', views.addProducto, name='addProducto'),
    
    # URLs del frontend integrado
    path('frontend/', views.frontend_home, name='frontend_home'),
    path('frontend/catalogo/', views.frontend_catalogo, name='frontend_catalogo'),
    path('frontend/catalogoVendedor/', views.frontend_catalogo_vendedor, name='frontend_catalogoVendedor'),
    path('agregar-carrito/<int:producto_id>/', views.agregarCarrito, name= 'agregarCarrito'),
    path('eliminar-carrito/<int:producto_id>/', views.eliminarCarrito, name= 'eliminarCarrito'),
    path('frontend/carrito/', views.frontend_carrito, name='frontend_carrito'),
    path('frontend/checkout/', views.frontend_checkout, name='frontend_checkout'),
    path('frontend/contacto/', views.frontend_contacto, name='frontend_contacto'),
    path('frontend/login/', views.frontend_login, name='frontend_login'),
    path('frontend/perfil/', views.frontend_perfil, name='frontend_perfil'),
    path('frontend/personaliza/', views.frontend_personaliza, name='frontend_personaliza'),
    path('frontend/signin/', views.frontend_signin, name='frontend_signin'),
    path('frontend/sobre/', views.frontend_sobre, name='frontend_sobre'),
]