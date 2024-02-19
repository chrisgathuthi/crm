from django.urls import include, path
from rest_framework import routers
from .views import (BandwidthView, ClientView, FieldWorkView,
                    MpesaTransactions, MpesaWebHook, ProviderView,
                    ShortMessageView, UserView, UserAuthenticateView, SmsWebHook, StaffView, MaterialView, SmsGatewayResponseView)

route = routers.DefaultRouter()
route.register("client", ClientView, basename="client")
route.register("fieldwork", FieldWorkView, basename="fieldwork")
route.register("sms", ShortMessageView, basename="sms")
route.register("registration", UserView, basename="registration")
route.register("sms-gateway-response",SmsGatewayResponseView, basename="smsgatewayresponse")
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
    path("login/",UserAuthenticateView.as_view({"post":"create"}),name="login"),
    path("bandwidth/",BandwidthView.as_view({"post":"create"}),name="bandwith"),
    path("bandwidthdestroy/",BandwidthView.as_view({"delete":"destroy"}),name="bandwith"),
    path("bandwidths/",BandwidthView.as_view({"get":"list"}),name="bandwith"),
    path("employee/",UserView.as_view({"post":"create"}),name="employee"),
    path("sms-callback/",SmsWebHook.as_view(),name="smswebhook"),
    path("staffs/",StaffView.as_view({"get":"list"}), name="staffs"),
    path("staff/",StaffView.as_view({"post":"create"}),name="staff"),
    path("material/",MaterialView.as_view({"post":"create"}),name="material"),
]
