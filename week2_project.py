"""
week2_project.py
----------------
Complete data fetcher script for Week 2 practice.
Features:
- Fetch Bitcoin price from CoinGecko API
- Handle errors (network issues, invalid data)
- Save results to CSV with timestamp
- Print success/failure message
"""

import requests
import csv
import os
from datetime import datetime

# -------------------------------
def fetch_bitcoin_price():
    """
    Fetch the current Bitcoin price in USD from CoinGecko API.
    Returns None if any error occurs.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        price = response.json()["bitcoin"]["usd"]
        return price
    except requests.exceptions.RequestException:
        print("Failed to connect to API")
    except KeyError:
        print("Invalid JSON structure")
    except ValueError:
        print("Error parsing JSON data")
    return None

# -------------------------------
def save_to_csv(symbol, price, timestamp=None):
    """
    Save price data to a CSV file with columns: timestamp, symbol, price.
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_path = os.path.join(os.path.dirname(__file__), "week2_prices.csv")
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "symbol", "price"])
        writer.writerow([timestamp, symbol, price])

# -------------------------------
def main():
    print("Starting Week 2 data fetcher...\n")
    symbol = "bitcoin"
    price = fetch_bitcoin_price()
    
    if price is not None:
        save_to_csv(symbol, price)
        print(f"✅ {symbol.capitalize()} price saved: ${price}")
    else:
        print(f"❌ Failed to fetch {symbol} price.")

# -------------------------------
if __name__ == "__main__":
    main()