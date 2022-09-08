from rest_framework import serializers

from .models import Trip


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = (
        'driver_id', 'vehicle_id', 'customer_id', 'address', 'cargo_tonnage', 'address_type', 'done_by_user_id',
        'created_at', 'updated_at')
