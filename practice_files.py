# Write data to a file
with open("test.txt", "w") as file:
    file.write("Hello, this is my first file.\n")
    file.write("Learning Python file handling.\n")


# Read data from the file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
    
# Append new data to the file
with open("test.txt", "a") as file:
    file.write("This line is added later.\n")
    