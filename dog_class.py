class Dog:

    animal_kind = "canine"
    # defining a class variable

    # function within the class
    def bark(self):
    # self refers to the current class ie Dog
        return "woof"

# To execute a class you have to create an instance of the class
fido = Dog()
# fido is an instance of the class Dog

# You can now call variables and functions from the Dog class
print(fido.animal_kind) # prints "Canine"
print(fido.bark()) # prints "woof"

# you can make changes to an instance of a class without changing the class itself
fido.animal_kind = "big dog"
print(fido.animal_kind) # prints "big dog"

# Another instance of the Dog class
lassie = Dog()
print(lassie.animal_kind)
# This prints out "Canine", not "big dog", because in the Dog class, the variable animal_kind is still set as "Canine"