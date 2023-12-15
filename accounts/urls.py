from django.urls import path, include
from .views import ClientView, FieldWorkView, BandwidthView, ShortMessageView, UserView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork")
route.register("bandwidth", BandwidthView, basename="bandwidth")
route.register("sms", ShortMessageView, basename="sms")
route.register("registration", UserView, basename="registration")
urlpatterns = [path("", include(route.urls))]
