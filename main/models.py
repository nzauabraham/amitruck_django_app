from django.db import models


class Trip(models.Model):
    driver_id = models.PositiveIntegerField()
    vehicle_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
