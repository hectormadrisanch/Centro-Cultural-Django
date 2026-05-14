from django.db import models

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} - {self.especializacion}"

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (Cap: {self.capacidad})"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    plazas_disponibles = models.IntegerField()
    
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, related_name='actividades')
    
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, related_name='actividades_principales')
    
    salas_secundarias = models.ManyToManyField(Sala, blank=True, related_name='actividades_secundarias')
    
    usuarios_inscritos = models.ManyToManyField(Usuario, blank=True, related_name='actividades')

    def __str__(self):
        return self.nombre