import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY' : apikey.API_KEY,
    'Accepts' : 'application/json'
}
currency = apikey.CCY
params = {
    'convert' : currency
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()
coins = json['data']
for x in coins:
    print(x['quote']['USDT']['price'])