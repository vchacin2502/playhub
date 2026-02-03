from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Juego(models.Model):
    PLATAFORMAS = [
        ('PC', 'PC'),
        ('PS', 'PlayStation'),
        ('XB', 'Xbox'),
        ('SW', 'Switch'),
    ]

    titulo = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=2, choices=PLATAFORMAS)

    precio = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]  # precio > 0
    )

    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    juego_titulo = models.CharField(max_length=100)
    usuario_username = models.CharField(max_length=150)

    puntuacion = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )

    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.juego_titulo} ({self.puntuacion}/10)"
