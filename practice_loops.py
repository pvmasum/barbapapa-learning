# List of prices
prices = [100, 105, 102, 108, 110]

# Loop through the list and print each price
for price in prices:
    print(price)
    

# Loop through prices and categorize them using if/else
# If the price is greater than 105 → High price
# Otherwise → Low price
prices = [100, 105, 102, 108, 110]

for price in prices:
    if price > 105:
        print("High price:", price)
    else:
        print("Low price:", price)



# Use a while loop to count from 1 to 10
count = 1

while count <= 10:
    print(count)
    count = count + 1