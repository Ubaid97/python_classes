# Created Cat class
class Cat:

    # declared two variables and passed integer values into them
    num_of_legs = 4
    num_of_whiskers = 6

    # function which returns the sound made by cats
    def sound(self):
        return "meow"

# Felix is an instance of the Cat class
felix = Cat()
felix.num_of_legs = 3
# changed the value of num_of_legs variables. this change only applies to this instance of the class
print("felix:")
# printing out all variables and function in this instance of the class
print(felix.num_of_legs) # prints out 3
print(felix.num_of_whiskers) # prints out 6
print(felix.sound()) # prints out "meow"

sully = Cat()
sully.num_of_whiskers = 5
print("sully:")
print(sully.num_of_legs) # prints out 4
print(sully.num_of_whiskers) # prints out 5
print(sully.sound())

inaya = Cat()
inaya.num_of_legs = 3
inaya_num_of_whiskers = 4
# changed the value of two variables in this instance of the Cat class
print("inaya:")
print(inaya.num_of_legs) # prints out 3
print(inaya.num_of_whiskers) # prints out 4
print(inaya.sound())

