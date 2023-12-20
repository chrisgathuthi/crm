from .models import MpesaTransaction, Provider, Client
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


def callback_parser(data = None):
    """
    parsing mpesa callback return a dict
    """
    pass
    

def save_mpesa_results(results = None) -> None:
    try:
       provider = Provider.objects.get(short_code=results["BusinessShortCode"])
       client = Client.objects.get(phone_number=results["MSISDN"])
    except ObjectDoesNotExist:
        pass# log this
    except Exception as e:
        print("There's an error here",e)
        pass
    else:
        MpesaTransaction.objects.create(
            provider=provider,
            client=client,
            transaction_type=results["TransactionType"],
            transaction_id=results["TransID"],
            transaction_time= datetime.strptime(results["TransTime"], "%Y%m%d%H%M%S"),
            transaction_amount= results["TransAmount"],
            short_code=results["BusinessShortCode"],
            invoice_number=results["InvoiceNumber"],
            bill_ref_number=results["BillRefNumber"],
            phone_number=results["MSISDN"],
            first_name=results["FirstName"],
            middle_name=results["MiddleName"],
            last_name=results["LastName"])
        return None    