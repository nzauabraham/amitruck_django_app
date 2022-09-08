from rest_framework import serializers


class TripSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()
    vehicle_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
    address = serializers.CharField()
    cargo_tonnage = serializers.DecimalField(max_digits=10, decimal_places=2)
    address_type = serializers.CharField()
    done_by_user_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

