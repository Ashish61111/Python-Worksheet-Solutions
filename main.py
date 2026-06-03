# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")


# Object creation
d = Dog()

# Accessing parent class method
d.sound()

# Accessing child class method
d.bark()