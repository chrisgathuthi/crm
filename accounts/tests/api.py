import requests
import json

url = "http://127.0.0.1:8000/api/accounts/completed-callback/"

payload = json.dumps({
  "TransactionType": "Pay Bill",
  "TransID": "RKTQDM9Q6S",
  "TransTime": "20231122063845",
  "TransAmount": "1000",
  "BusinessShortCode": "123456",
  "BillRefNumber": "HT8797",
  "InvoiceNumber": "",
  "OrgAccountBalance": "",
  "ThirdPartyTransID": "",
  "MSISDN": "254757164343",
  "FirstName": "Jane",
  "MiddleName": "Chris",
  "LastName": "Doe"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=TDj9Knmq3rWVRqmFnAg4ii3QZEqknBJn'
}
for i in range(200):

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

