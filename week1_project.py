# Simple Price Tracker for 3 Iranian stocks
import random

# List of stock symbols
symbols = ["فملی", "فولاد", "خودرو"]

# Open a file to save all prices
# Loop through each symbol
# Generate a fake price between 1000 and 10000
# Write the symbol and price to the file
with open("prices.txt", "w", encoding="utf-8") as file:
    for symbol in symbols:
        price = random.randint(1000, 10000)
        file.write(f"{symbol}: {price}\n")
        
#Print summary
print(f"Prices saved for {len(symbols)} symbols")