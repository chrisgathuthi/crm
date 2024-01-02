from django.urls import path, include
from .views import ClientView, FieldWorkView, BandwidthView, ShortMessageView, UserView, ProviderView, MpesaWebHook, MpesaTransactions
from rest_framework import routers

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork")
route.register("bandwidth", BandwidthView, basename="bandwidth")
route.register("sms", ShortMessageView, basename="sms")
route.register("registration", UserView, basename="registration")
urlpatterns = [
    path("", include(route.urls)),
    path("provider/",ProviderView.as_view({"post":"create"}), name="create-provider"),
    path("completed-callback/",MpesaWebHook.as_view(),name="completed-url"),
    path("shortmessage/",ShortMessageView.as_view({"post":"create"}), name="shortmessage"),
    path("shortmessages/",ShortMessageView.as_view({"get":"list"}), name="shortmessages"),
    path("mpesatransactions/", MpesaTransactions.as_view({"get":"list"}),name="mpesatransactions")
]
