from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Trip


class TripView(APIView):
    def get(self, request):
        trip_logs = Trip.objects.all()
        return Response({"trip_logs": trip_logs})
