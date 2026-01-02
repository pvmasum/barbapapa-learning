# data_fetcher.py
# -------------------------------
import requests                   # For sending HTTP requests
import csv                        # For handling CSV files
import os                         # For file path operations
from datetime import datetime     # For timestamping

def fetch_crypto_price(symbol):
    
    """
    Fetch the current price of a cryptocurrency in USD.
    Returns None if any error occurs.
    """
    
    print(f"Fetching price for {symbol}...")
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)     # Send GET request with a 10s timeout
        response.raise_for_status()                  # Raise an exception for HTTP errors
        price = response.json()[symbol]["usd"]       # Extract the price from JSON response
        print("Price fetched successfully")
        return price
    except requests.exceptions.RequestException:
        print("Failed to connect to API")            # Network/API connection error
    except KeyError:
        print("Invalid symbol or response format")   # Symbol not found in response
    except ValueError:
        print("Error parsing JSON data")             # JSON parsing error
    return None

def save_price_to_csv(symbol, price, timestamp=None):
   
    """
    Save cryptocurrency price to a CSV file with columns: timestamp, symbol, price.
    Timestamp defaults to current time up to seconds if not provided.
    """
    
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    # Current time in YYYY-MM-DD HH:MM:SS format

    # CSV file path in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "prices.csv")
    file_exists = os.path.isfile(file_path)                         # Check if CSV already exists

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)                                   # Initialize CSV writer
        if not file_exists:                                         # Write header only if file is new
            writer.writerow(["timestamp", "symbol", "price"])
        writer.writerow([timestamp, symbol, price])                 # Write price record

    print(f"Price for {symbol} saved to CSV")

# -------------------------------
# Test & save prices
symbols = ["bitcoin", "ethereum", "invalid_symbol"]
for s in symbols:
    price = fetch_crypto_price(s)
    if price is not None:
        save_price_to_csv(s, price)
    


























