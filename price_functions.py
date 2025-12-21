# get_price function
# #returns a fake price for Iranian stock market symbols
def get_price(symbol):
    fake_prices = {
        "خساپا": 2850,
        "فولاد": 19500,
        "شستا": 1120,
        "فملی": 8650,
        "وبملت": 3250,
        "کچاد": 14200,
        "شپنا": 9800
    }

    return fake_prices.get(symbol, 0)

# EX:
print(get_price("خساپا"))
print(get_price("خودرو")) 


# calculate_change function
# #returns percentage change between old and new price
def calculate_change(old_price, new_price):
    if old_price == 0:
        return 0
    return ((new_price - old_price) / old_price) * 100

# Ex:
symbol = "خساپا"
old_price = get_price(symbol)
new_price = 3100  

change = calculate_change(old_price, new_price)

print("Symbol:", symbol)
print("Old price (Rial):", old_price)
print("New price (Rial):", new_price)
print("Price change (%):", change)