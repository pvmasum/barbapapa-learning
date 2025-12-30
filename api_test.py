"""
api_test.py
------------
Fetches the current Bitcoin price in USD using the CoinGecko API.
"""

import requests

# CoinGecko API endpoint
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract Bitcoin price in USD
bitcoin_price = data["bitcoin"]["usd"]

# Print result
print(f"Bitcoin price: ${bitcoin_price}")
