import data
import requests

API_KEY = 'fca_live_f8p9ih55ht3hf6qwP3JTGkJFfSW66C9XDJi7HFi8'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ['USD', "CAD", "EUR", "AUD", "CNY"]


def currency_converter(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data["data"]

    except :
        print("Invalid currency.")
        return None


while True:
        base =input("Enter the base currency you want to convert(Q for quit: ").upper()
        if base =="Q":
            break
        data= currency_converter(base)
        if not data:
            continue
del data[base]
for ticker, value in data.items():
    print(f"{ticker}:{value}")

