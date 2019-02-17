import requests
import json

key = "1472762928494a6da6b27184b02a6af8";

def queryAPIForProduct(ID):
    get_url = 'https://api.wegmans.io/products/{sku}?api-version=2018-10-18'
    get_url = get_url.replace('{sku}', str(ID))
    headers = {
        'Subscription-Key': key,
    }
    r = requests.get(get_url, headers=headers)
    rd = json.loads(r.text)

    toReturn = str(rd['name']) + ":" + str(rd['tradeIdentifiers'][0]['images'])

    print('Request data ' + toReturn)

def queryAPIForRecipe(ID) -> str:
    get_url = 'https://api.wegmans.io/meals/recipes/{id}?api-version=2018-10-18'
    get_url = get_url.replace('{id}', str(ID))
    headers = {
        'Subscription-Key': key,
    }
    r = requests.get(get_url, headers=headers)
    rd = json.loads(r.text)

    toReturn = str(rd['name']) + ":" + str(rd['_links'][2]['href'])

    return toReturn

#def getProduct(ID):