import http.client

conn = http.client.HTTPConnection("api,wegmans,io")

payload = ""

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "eed96f4c-9c5b-4857-b1fb-30949ed241a7",
    'Subscription-Key': "510bfc0b0c0a487fba05de17c35d7954"
    }

conn.request("GET", "meals,recipes", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))