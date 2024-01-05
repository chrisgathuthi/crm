from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Client, MpesaTransaction, Provider


def callback_parser(data=None):
    """
    parsing mpesa callback return a dict
    """
    pass


def save_mpesa_results(results=None) -> None:
    try:
        provider = Provider.objects.get(short_code=results["BusinessShortCode"])
        client = Client.objects.get(serial=results["BillRefNumber"])
    except ObjectDoesNotExist:
        pass  # log this
    else:
        MpesaTransaction.objects.create(
            provider=provider,
            client=client,
            transaction_type=results["TransactionType"],
            transaction_id=results["TransID"],
            transaction_time=datetime.strptime(results["TransTime"], "%Y%m%d%H%M%S"),
            transaction_amount=results["TransAmount"],
            short_code=results["BusinessShortCode"],
            invoice_number=results["InvoiceNumber"],
            bill_ref_number=results["BillRefNumber"],
            phone_number=results["MSISDN"],
            first_name=results["FirstName"],
            middle_name=results["MiddleName"],
            last_name=results["LastName"],
        )
        # return None


def get_user_from_token(header=None):
    """parse auth header to get user"""

    user_token = header.get("HTTP_AUTHORIZATION").split()[1]

    try:
        user = Token.objects.get(key=user_token)
    except Token.DoesNotExist:
        return {"message": "No token found proceed to login"}
    else:
        return user


def get_provider_from_token(header=None):
    """parse auth header to get provider"""

    user_token = header.get("HTTP_AUTHORIZATION").split()[1]

    try:
        user = Token.objects.get(key=user_token)
    except Token.DoesNotExist:
        return {"message": "No token found proceed to login"}
    else:
        provider = Provider.objects.get(owner=user.user)
        return provider
