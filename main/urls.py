from django.urls import include, path
from rest_framework import routers
from .views import TripView

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('trip/', TripView.as_view())
]