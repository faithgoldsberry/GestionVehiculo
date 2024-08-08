from django.db import models

class Vehiculo(models.Model):
    vin = models.CharField(max_length=17, unique=True, primary_key=True)  # Usa VIN como clave primaria
    motor = models.CharField(max_length=50, unique=True)
    cilindrada = models.IntegerField()
    ano = models.PositiveIntegerField()
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    dueno = models.CharField(max_length=50, default='Dueño')

    def __str__(self):
        return f"{self.vin} {self.modelo} {self.ano}"

class Placa(models.Model):
    patente = models.CharField(max_length=20, unique=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='placas') # Permite sin placa patente o con múltiples placas

    def __str__(self):
        return self.patente
