from django.contrib import admin
from .models import Juego, Resena

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio', 'fecha_lanzamiento')
    search_fields = ('titulo',)
    list_filter = ('plataforma',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('juego_titulo', 'usuario_username', 'puntuacion', 'fecha')
    search_fields = ('juego_titulo', 'usuario_username')
