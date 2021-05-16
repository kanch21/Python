#Try/except

str = 'Hello Kanchan'
try:
    istr = int(str)
except:
    istr = -1

print('First',istr)

str= 123
try:
    istr = int(str)
except:
    istr = -1

print('Second',istr)


#Sample 2- real world problem

num = input("enter a number: ")
try:
    ival = int(num)
except:
    ival = -1

if ival > 0:
    print("valid number!")
else:
    print("invalid number")