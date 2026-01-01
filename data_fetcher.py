# data_fetcher.py
# ----------------
# Fetch cryptocurrency prices in USD using the CoinGecko API

import requests


def fetch_crypto_price(symbol):
    """Return crypto price in USD or None if an error occurs."""

    # Status message: start fetching
    print(f"Fetching price for {symbol}...")

    # Dynamic API URL based on symbol
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

    try:
        # Send HTTP GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Extract nested price value
        price = data[symbol]["usd"]

        # Status message: success
        print("Price fetched successfully")
        return price

    except requests.exceptions.RequestException:
        # Network or HTTP-related errors
        print("Failed to connect to API")

    except KeyError:
        # Invalid symbol or unexpected JSON structure
        print("Invalid symbol or response format")

    except ValueError:
        # JSON parsing errors
        print("Error parsing JSON data")

    # Return None if any error occurs
    return None


# Simple test cases
print(fetch_crypto_price("bitcoin"))
print(fetch_crypto_price("ethereum"))
print(fetch_crypto_price("invalid_symbol"))
