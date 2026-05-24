from django.db import models


class Recurso(models.Model):
    titulo      = models.CharField(max_length=200)
    url         = models.URLField()
    descripcion = models.TextField(blank=True)
    creado      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering      = ['-creado']
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo


class Mensaje(models.Model):
    nombre   = models.CharField(max_length=100)
    correo   = models.EmailField()
    mensaje  = models.TextField()
    recibido = models.DateTimeField(auto_now_add=True)
    leido    = models.BooleanField(default=False)

    class Meta:
        ordering      = ['-recibido']
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return f"{self.nombre} — {self.recibido.strftime('%d/%m/%Y')}"
