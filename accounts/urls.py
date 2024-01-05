from django.urls import include, path
from rest_framework import routers

from .views import (BandwidthView, ClientView, FieldWorkView,
                    MpesaTransactions, MpesaWebHook, ProviderView,
                    ShortMessageView, UserView)

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork")
route.register("bandwidth", BandwidthView, basename="bandwidth")
route.register("sms", ShortMessageView, basename="sms")
route.register("registration", UserView, basename="registration")
urlpatterns = [
    path("", include(route.urls)),
    path("provider/", ProviderView.as_view({"post": "create"}), name="create-provider"),
    path(
        "provider-detail/",
        ProviderView.as_view({"get": "retrieve"}),
        name="retrieve-provider",
    ),
    path("completed-callback/", MpesaWebHook.as_view(), name="completed-url"),
    path(
        "shortmessage/",
        ShortMessageView.as_view({"post": "create"}),
        name="shortmessage",
    ),
    path(
        "shortmessages/",
        ShortMessageView.as_view({"get": "list"}),
        name="shortmessages",
    ),
    path(
        "mpesatransactions/",
        MpesaTransactions.as_view({"get": "list"}),
        name="mpesatransactions",
    ),
    path(
        "mpesatransaction/",
        MpesaTransactions.as_view({"get": "retrieve"}),
        name="mpesatransactions",
    ),
]
