#Functions are used for storing and reusing
#user defined function

#Function 1
#Parameters are the values that are passed in the function definition
def num_selection(x):     #function definition
    print(f'the number you chose is {x}')

num=input('enter a number:')
#Arguments are the values which we use while calling a function
num_selection(num)        #function call
print('end of function')


#Function 2- having return values
#using return- return is like a break in function which ends the function execution and returns a value to the function.

def greet():
    c = 21
    return c

print("Kanchan_",greet())


#Function 3- adding multiple parameters

def add(x,y):
    sum = x+y
    return sum

print("The sum of 5 and 4 is ",add(5,4))

#Built-in function

big_letter=max('Kanchan Chowdhari')
print(big_letter)

small_letter=min('KanchanChowdhari')
print(small_letter)

num1 = 20
print(type(num1))