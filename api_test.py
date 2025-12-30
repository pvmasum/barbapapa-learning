"""
api_test.py
Fetches the current Bitcoin price in USD using the CoinGecko API.
"""

import requests

# API endpoint
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Check HTTP status

    data = response.json()       # Parse JSON response
    bitcoin_price = data["bitcoin"]["usd"]  # Extract nested value

    print(f"Bitcoin price: ${bitcoin_price}")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except KeyError:
    print("Unexpected JSON structure.")

except ValueError:
    print("Failed to parse JSON response.")
    
    