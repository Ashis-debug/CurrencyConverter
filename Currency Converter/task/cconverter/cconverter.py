import requests
import json
currency_you_have = input().lower()
cache = {}
newCurrency = requests.get("http://www.floatrates.com/daily/" + currency_you_have + ".json").json()
if currency_you_have == 'usd':
    cache = {
             'eur': newCurrency['eur']['rate']
             }
elif currency_you_have == 'eur':
    cache = {
        'usd': newCurrency['usd']['rate']
    }
else:
    cache = {
        'usd': newCurrency['usd']['rate'],
        'eur': newCurrency['eur']['rate']
    }
while True:
    currency_to_exchange = input().lower()
    if currency_to_exchange == "":
        break
    amount = float(input())
    print("Checking the cache...")
    if currency_to_exchange in cache:
        print("Oh! It is in the cache!")
        result = amount * cache[currency_to_exchange]
        print(f"You received {round(result, 2)} {currency_to_exchange.upper()}")
    else:
        print("Sorry, but it is not in the cache!")
        new_currency = requests.get("http://www.floatrates.com/daily/" + currency_you_have + ".json").json()
        cache[currency_to_exchange] = new_currency[currency_to_exchange]['rate']
        result = amount * cache[currency_to_exchange]
        print(f"You received {round(result, 2)} {currency_to_exchange.upper()}")






