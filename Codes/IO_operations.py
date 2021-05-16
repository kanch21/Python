#user input
input_var = input("Please enter your name")
print(f"My name is {input_var}")

#converting user input
#note input() returns a string value
inp= input('Europe Floor?')
#usfloor= inp + 1
#if not typecasted we get the below error
#TypeError: can only concatenate str (not "int") to str
usfloor=int(inp) +1  #typecasted to int here
print('US floor:',usfloor)