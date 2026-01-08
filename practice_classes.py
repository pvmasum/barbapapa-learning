# Define a Dog class as a blueprint for dog objects
class Dog:
    def __init__(self, name, age):
        # Initialize object attributes
        self.name = name
        self.age = age

    def bark(self):
        # Instance method that uses object data
        print(f"{self.name} says: Woof! ")
        

# Create an object (instance) of the Dog class        
my_dog = Dog("Buddy", 3)
# Call a method on the object
my_dog.bark()

# Access object attributes
print(my_dog.name)
print(my_dog.age)