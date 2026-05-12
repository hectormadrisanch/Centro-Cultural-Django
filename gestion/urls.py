from django.urls import path
from . import views

urlpatterns = [
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', views.crear_actividad, name='crear_actividad'),
    path('actividades/<int:id>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('actividades/<int:id>/editar/', views.editar_actividad, name='editar_actividad'),
]