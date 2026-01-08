"""
price_tracker.py
----------------
Fetches cryptocurrency prices from an API and stores them in a CSV file
class-based structure.
"""

import requests
import csv
import os
from datetime import datetime


class PriceTracker:
    """
    A class responsible for fetching cryptocurrency prices
    and saving them into a CSV file.
    """

    def __init__(self, csv_filename="crypto_prices_week3.csv"):
        # Store CSV file in the same directory as this script
        self.file_path = os.path.join(os.path.dirname(__file__), csv_filename)

    def fetch_price(self, symbol):
        """
        Fetch the current price of a cryptocurrency in USD.
        Returns the price if successful, otherwise None.
        """
        print(f"Fetching price for {symbol}...")
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            price = data[symbol]["usd"]

            print("Price fetched successfully")
            return price

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")

        except KeyError:
            print("Invalid symbol or unexpected API response")

        except ValueError:
            print("Failed to parse JSON response")

        return None

    def save_price(self, symbol, price):
        """
        Save the fetched price to a CSV file with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.isfile(self.file_path)

        with open(self.file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            # Write header only once
            if not file_exists:
                writer.writerow(["timestamp", "symbol", "price"])

            writer.writerow([timestamp, symbol, price])

        print(f"{symbol.capitalize()} price saved: ${price}")


# Run (Week 3 test)
if __name__ == "__main__":
    print("Starting Week 3 price tracker...\n")

    tracker = PriceTracker()
    symbol = "bitcoin"

    price = tracker.fetch_price(symbol)

    if price is not None:
        tracker.save_price(symbol, price)
    else:
        print("Price was not saved due to an error")