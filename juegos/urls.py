from django.urls import path
from .views import *

urlpatterns = [
    path('juegos/', JuegoListView.as_view(), name='juego_list'),
    path('juegos/nuevo/', JuegoCreateView.as_view(), name='juego_create'),
    path('juegos/<int:pk>/editar/', JuegoUpdateView.as_view(), name='juego_update'),
    path('juegos/<int:pk>/borrar/', JuegoDeleteView.as_view(), name='juego_delete'),

    path('resenas/', ResenaListView.as_view(), name='resena_list'),
    path('resenas/nueva/', ResenaCreateView.as_view(), name='resena_create'),
    path('resenas/<int:pk>/editar/', ResenaUpdateView.as_view(), name='resena_update'),
    path('resenas/<int:pk>/borrar/', ResenaDeleteView.as_view(), name='resena_delete'),
]
