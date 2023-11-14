from django.urls import path, include
from .views import ClientView, FieldWorkView, BandwidthView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork")
route.register("bandwidth", BandwidthView, basename="bandwidth")
urlpatterns = [path("", include(route.urls))]
