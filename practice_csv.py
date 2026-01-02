import csv

# Create and write to CSV file
with open("prices.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["timestamp", "symbol", "price"])

    # Write sample rows
    writer.writerow(["2025-01-01 10:00", "bitcoin", 43000])
    writer.writerow(["2025-01-01 10:01", "ethereum", 2300])

print("CSV file created and data written.")


# Read CSV file
with open("prices.csv", mode="r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        
# Append new row to CSV
with open("prices.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["2025-01-01 10:02", "bitcoin", 43120])

print("New row appended.")