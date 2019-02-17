import requests
import json

key = "1472762928494a6da6b27184b02a6af8";

def grabProduct(ID):
    get_url = 'https://api.wegmans.io/products/{sku}?api-version=2018-10-18'
    get_url = get_url.replace('{sku}', str(ID))
    headers = {
        'Subscription-Key': key,
    }
    r = requests.get(get_url, headers=headers)
    rd = json.loads(r.text)

    print('Request data ' + str(rd))

grabProduct(11914)