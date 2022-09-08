from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Trip
from .serializers import TripSerializer


class TripView(APIView):
    def get(self, request):
        trip_logs = Trip.objects.all()
        serializer = TripSerializer(trip_logs, many=True)
        return Response({"trip_logs": serializer.data})
