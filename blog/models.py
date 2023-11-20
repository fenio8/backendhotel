from django.db import models

# Create your models here.


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    username = models.CharField(max_length=100)
    comentario = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Comentario de {self.username} en {self.tipo_habitacion.nombre}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.username
