from django.urls import path, include
from .views import ClientView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")

urlpatterns = [
    path("", include(route.urls))
]
print(route.urls)
