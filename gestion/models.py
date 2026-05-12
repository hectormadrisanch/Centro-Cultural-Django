from django.db import models

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)
    
    # Este método hace que en el panel de admin salga el nombre en vez de "Monitor object (1)"
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
    # Relación 1 a 1: Cada sala tiene un único responsable técnico
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
    
    # Relación 1 a N: Una actividad la da UN monitor (pero un monitor da muchas)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, related_name='actividades')
    
    # Relación 1 a N: Una actividad tiene UNA sala principal
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, related_name='actividades_principales')
    
    # Relación N a N: Una actividad puede usar varias salas secundarias, y una sala secundaria usarse en varias actividades
    salas_secundarias = models.ManyToManyField(Sala, blank=True, related_name='actividades_secundarias')
    
    # Relación N a N: Muchos usuarios en muchas actividades
    usuarios_inscritos = models.ManyToManyField(Usuario, blank=True, related_name='actividades')

    def __str__(self):
        return self.nombre