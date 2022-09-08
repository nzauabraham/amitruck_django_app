from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Trip(models.Model):
    driver_id = models.PositiveIntegerField()
    vehicle_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    address = models.CharField(max_length=50, null=True)
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    AddressType = (
        ('pickup_point', 'pickup_point'),
        ('drop_off_point', 'drop_off_point'),
    )
    address_type = models.CharField(max_length=50, choices=AddressType, null=True)
    done_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
