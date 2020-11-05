# Python classes
## Object-Oriented Programming
### 4 pillars
- Inheritance 
    - Eliminates redundant code
    - Allows the use of functions and variables from a parent class
- Encapsulation 
    - Reduces complexity and increases reusability
    - 
- Abstraction 
    - Reduces complexity and isolate impact of changes
- Polymorphism 
    - Refactor code or case statements
    - Allows us to change behaviours or attributes/variables
- Classes are the main tools for implementing these pillars
- Classes are a way of bringing data and functionality together
### Creating a class
````
class Name_of_class:
# Class name must start with a capital letter
````
### Executing a class
- Here's a class, with a variable and a function:
````
class Dog:

    animal_kind = "canine"
    # defining a class variable

    # function within the class
    def bark(self):
    # self refers to the current class ie Dog
        return "woof"
````
- To execute the class, you have to create an instance of the class
```
fido = Dog()
# fido is an instance of the Dog class
```
- You can now call variables and functions from the Dog class
```
print(fido.animal_kind) # prints "Canine"
print(fido.bark()) # prints "woof"
```
- You can make changes to an instance of a class without changing the class itself
```
fido.animal_kind = "big dog"
print(fido.animal_kind) # prints "big dog"
```
- Now if you create another instance of the same class,
```
lassie = Dog()
print(lassie.animal_kind) # prints "Canine"
```
- This prints out "Canine", not "big dog", because in the Dog class, the variable animal_kind is still set as "Canine". it's only been changed to "big dog" in the fido instance of the class

### initialising a class
