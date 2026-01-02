# data_fetcher.py (short & clean)
# -------------------------------
import requests
import csv
import os
from datetime import datetime

def fetch_crypto_price(symbol):
    """Fetch crypto price in USD or return None if error."""
    print(f"Fetching price for {symbol}...")
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        price = response.json()[symbol]["usd"]
        print("Price fetched successfully")
        return price
    except requests.exceptions.RequestException:
        print("Failed to connect to API")
    except KeyError:
        print("Invalid symbol or response format")
    except ValueError:
        print("Error parsing JSON data")
    return None

def save_price_to_csv(symbol, price, timestamp):
    """Save price to CSV with columns: timestamp, symbol, price."""
    file_path = os.path.join(os.path.dirname(__file__), "prices.csv")
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:  # write header only once
            writer.writerow(["timestamp", "symbol", "price"])
        writer.writerow([timestamp, symbol, price])

    print(f"Price for {symbol} saved to CSV")

# -------------------------------
# Test & save prices
symbols = ["bitcoin", "ethereum", "invalid_symbol"]
for s in symbols:
    price = fetch_crypto_price(s)
    if price is not None:
        save_price_to_csv(s, price, datetime.now())
    


























