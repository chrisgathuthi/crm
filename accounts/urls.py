from django.urls import path, include
from .views import ClientView, FieldWorkView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork" )
urlpatterns = [
    path("", include(route.urls))
]