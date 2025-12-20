stocks = ["خساپا", "فولاد", "شستا", "فملی", "وبملت"]

print(stocks)

stocks.append("خودرو")
stocks.remove("شستا")
print(stocks)


# Dictionary of stock prices (example values)
prices = {
    "خساپا": 3200,
    "فولاد": 5200,
    "فملی": 4800
}

print(prices)

# Access a value
print("Price of فولاد:", prices["فولاد"])

# Modify a value
prices["فولاد"] = 5400

# Add a new stock price
prices["وبملت"] = 3900

print(prices)