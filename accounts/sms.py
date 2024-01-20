import http.client
import json

conn = http.client.HTTPSConnection("2v1yql.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"254776082635"}],
            "from": "ServiceSMS",
            "text": "Hello,\n\nThis is a test message from Infobip. Have a nice day!"
        }
    ]
})
headers = {
    'Authorization': 'App f4e85feebeea1527baca68f92c09ff96-3bf4ad20-1a6c-4d5f-b872-1271295637d4',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))