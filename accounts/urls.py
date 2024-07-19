from django.urls import include, path
from rest_framework import routers
from .views import (BandwidthView, ClientView, FieldWorkView,
                    MpesaTransactions, MpesaWebHook, ProviderView,
                    ShortMessageView, UserView, UserAuthenticateView, SmsWebHook, EmployeeView, MaterialView, SmsGatewayResponseView, InventoryView)

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
    path("staffs/",EmployeeView.as_view({"get":"list"}), name="employees"),
    path("staff/",EmployeeView.as_view({"post":"create"}),name="employee"),
    path("staff/<int:pk>/",EmployeeView.as_view({"get":"retrieve"}),name="employee-detail"),
    path("staff/change/<int:pk>/",EmployeeView.as_view({"patch":"partial_update"}),name="employee-detail"),
    path("material/",MaterialView.as_view({"post":"create"}),name="material"),
    path("inventory/",InventoryView.as_view({"post":"create"}),name="create-inventory"),
    path("inventory/<int:pk>/",InventoryView.as_view({"get":"retrieve"}),name="create-inventory"),
    path("inventory/<int:pk>/update/",InventoryView.as_view({"patch":"partial_update"}),name="create-inventory"),
    path("inventories/",InventoryView.as_view({"get":"list"}),name="inventory-list")
]
