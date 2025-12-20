# My stock portfolio (example prices)
portfolio = {
    "خساپا": 3200,
    "فولاد": 5400,
    "فملی": 4800
}

print("My Portfolio:")

for stock, price in portfolio.items():
    print(stock, ":", price, "Toman")
    
total_value = 0

for price in portfolio.values():
    total_value += price

print("Total Portfolio Value:", total_value, "Toman")