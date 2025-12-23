# List of prices
prices = [100, 105, 102, 108, 110]

# Loop through prices and generate signals
for price in prices:
    if price > 105:
        print("BUY signal")
    else:
        print("HOLD")