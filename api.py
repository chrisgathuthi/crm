import requests
from django.conf import settings
from decouple import config
import json

data = {
    "from": "TIARACONECT",
    "to": "25457164343",
    "message": "Hello world people",
    "refId": "hdb212-0351/2019"
}

response = requests.post(url="https://api.tiaraconnect.io/api/messaging/sendsms", data=json.dumps(data),
                         headers={"Authorization": f"Bearer {config('SMSAPIKEY')}", 'Content-Type': 'application/json'})
print(response.text)
