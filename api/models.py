from django.db import models

class Port(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Trajet(models.Model):
    port_depart = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='trajets_depart')
    port_arrivee = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='trajets_arrivee')
    date_depart = models.DateField()
    duree_estimee = models.IntegerField(help_text='Durée estimée en heures')
    emission_co2 = models.FloatField(help_text='Émissions CO2 estimées en kg')

    def __str__(self):
        return f'{self.port_depart} -> {self.port_arrivee} le {self.date_depart}'
