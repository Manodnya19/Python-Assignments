# Q31.py

# ---------- Single Inheritance ----------
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks")


# ---------- Multiple Inheritance ----------
class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

class Child(Father, Mother):  # Multiple inheritance
    def skills(self):
        print("Child inherits skills from both parents")


# ---------- Multilevel Inheritance ----------
class Grandparent:
    def heritage(self):
        print("Grandparent: Shares legacy")

class Parent(Grandparent):  # Level 1
    def guide(self):
        print("Parent: Provides guidance")

class Son(Parent):  # Level 2
    def learn(self):
        print("Son: Learning from ancestors")


# ---------- Example Usage ----------

# Single Inheritance
print("Single Inheritance Example:")
dog = Dog()
dog.speak()
dog.bark()

print("\nMultiple Inheritance Example:")
# Multiple Inheritance
child = Child()
child.skills()

print("\nMultilevel Inheritance Example:")
# Multilevel Inheritance
son = Son()
son.heritage()
son.guide()
son.learn()
