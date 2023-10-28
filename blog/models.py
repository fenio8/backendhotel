from django.db import models

# Create your models here.

class Comentario(models.Model):
    username = models.CharField(max_length=100)
    comentario = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Review"
        verbose_name_plural="Reviews"
    
    def __str__(self):
        return self.username
