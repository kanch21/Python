# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Note- in print(), f is the formatted string literal which accepts variable values at runtime

College = 'University of South Florida'
print(f"I belong to the {College}")

#other way of writing print()
print("I belong to the ",College,"which is based out of Tampa!")


#handling numeric datatypes

#usecase 1
distance = 10
time = 1.5
speed = distance*time
print(f"The speed of the car is {speed}\n")

#usecase 2
result = 20 + 3 * 5 / 3
print(f"The result of the expression is {result}\n")

#printing datatypes
intnum= 5
print("type of intnum is ",type(intnum))

floatnum= 5.3
print("type of floatnum is ",type(floatnum))

bool= True
print("type of bool is ",type(bool))

# handling string type

name = 'Kanchan'
print(f"Hello {name}!")

typeofname=type(name)
print(f"the datatype of name variable is {typeofname}")

fullname= 'kanchan ' + 'chowdhari'
print(f"full name is {fullname}")