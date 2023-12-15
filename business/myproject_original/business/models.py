from django.contrib.gis.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    coordinates = models.PointField()

    def __str__(self):
        return self.name