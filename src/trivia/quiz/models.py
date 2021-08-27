from django.db import models

class Pregunta(models.Model):
    enunciado = models.CharField(max_length=500)
    categoria = models.CharField(max_length=20)
    def __str__(self):
        return self.enunciado


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    correcto = models.CharField(max_length=2)
    def __str__(self):
        return self.texto_opcion


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    usuario = models.IntegerField(default=0)  
    puntaje = models.IntegerField(default=0)
    def __str__(self):
        return str(self.opcion)

