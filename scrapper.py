import requests
import csv
from datetime import datetime

CURRENCIES = ['bitcoin', 'ethereum', 'solana']
csvFile = 'prices.csv'

def fetch_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(CURRENCIES),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = []
    time = datetime.now().strftime('%Y-%m-%d %H:%M')
    for coin in CURRENCIES:
        price = data[coin]['usd']
        prices.append((time, coin, price))
    return prices

def csvsave(prices):
    file_exists = False
    try:
        with open(csvFile, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(csvFile, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['TIMESTAMP', 'COIN', 'PRICE(USD)'])
        writer.writerows(prices)

if __name__ == "__main__":
    prices = fetch_prices()
    csvsave(prices)
    print("Prices fetched and saved to prices.csv!")
