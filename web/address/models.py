from django.db import models
from django.contrib.gis.db import models as gismodels


class shop(models.Model):
    name = models.CharField(max_length=100)
    location = gismodels.PointField()
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    @property
    def loc(self):
        return shop.location
