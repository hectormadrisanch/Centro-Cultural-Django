from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='inicio'),

    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', views.crear_actividad, name='crear_actividad'),
    path('actividades/<int:id>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('actividades/<int:id>/editar/', views.editar_actividad, name='editar_actividad'),

    #usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    # Monitores
    path('monitores/', views.lista_monitores, name='lista_monitores'),
    path('monitores/nuevo/', views.crear_monitor, name='crear_monitor'),
    path('monitores/<int:id>/', views.detalle_monitor, name='detalle_monitor'),
    path('monitores/<int:id>/editar/', views.editar_monitor, name='editar_monitor'),
    path('monitores/<int:id>/eliminar/', views.eliminar_monitor, name='eliminar_monitor'),
]