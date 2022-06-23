from django.db import models


class Data(models.Model):
    sensor_type = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)
