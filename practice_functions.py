# greet function
# #prints greeting message using given name
def greet(name):
    print("Welcome", name)
    
greet("Elina")


# add function
# #returns the sum of two numbers
def add(a, b):
    return a + b

result = add(17, 6)
print(result)


# greet_user function
# #uses default argument if no name is provided
def greet_user(name="Reza"):
    print("Nice to meet you", name)
    
greet_user("Elina")
greet_user("Reza")


