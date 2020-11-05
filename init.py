class Dog:

    animal_kind = "canine"

    # Initialising Dog class
    def __init__(self, name, colour):
        # value passed as name in class object will be saved as object_name.name
        self.name = name
        # value passed as colour in class object will be saved as object_name.colour
        self.colour = colour

    def bark(self):
        return "woof"

fido = Dog("Fido", "brown")
# "Fido" is the value passed into the variable 'name'
# "brown" is the value passed into the variable 'colour'

print(fido.name) # self.name = fido.name in this instance. See line 7
print(fido.colour) # self.colour = fido.colour in this instance. See line 9