import csv

# Save symbol and price to prices.csv
def save_price(symbol, price):
    with open("prices.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([symbol, price])
        

# Read and print the last 5 prices
def read_prices():
    with open("prices.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        # Get last 5 rows
        last_rows = rows[-5:]

        for row in last_rows:
            print(row)
            

# Test the functions
save_price("AAPL", 180)
save_price("AAPL", 182)
save_price("AAPL", 179)
save_price("AAPL", 185)
save_price("AAPL", 190)
save_price("AAPL", 195)

read_prices()