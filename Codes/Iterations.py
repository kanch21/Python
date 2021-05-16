
#while loop- this is a indefinite loop which iterates until it gets a false bool value.
# use case 1 -definite loop
n = 5
while n > 0:
    print(n)
    n = n-1
print("end of while loop")
print(n)

#while loop-
# use case 2- indefinite loop
# n = 5
# while n > 0:
#     print(n)
#     print("unending loop")


#use case 3 - no loop
n = 0
while n > 0:
    print(n)
    print("unending loop")
print("out of loop")

#implementing break statement
#break statement breaks the loop execution and gets out of the loop.
while True:
    line = input("enter text:")
    if line == "Done!":
        break
    print(line)
print("end of text entering!")

#continue statement- it stops the current execution and goes on top of the loop to run the loop again.

while True:
    line = input("enter text:")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("out of while loop")

#for loops-it is a definite loop because it runs an exact number of times

#simple for loop
# we do not use range() but explicitly mention the list through which you should iterate
for i in [5, 3, 1]:
    print(i)
print("end of for loop")

#for strings
for i in ["Kanchan", "Sourav", "Sharma"]:
    print(i)
print("end of for loop")

#other way of doing the above execution-
names = ["Kanchan", "Sourav", "Sharma"]   #used lists
for name in names:
    print(name)
print("end of names!")

#finding the largest number in the list
lists = [3, 41, 12, 74, 15, 9]
largest_num = -1
#i = 0
for i in lists:   #always remember- the iterator i should hold the same value as of list elements
    if largest_num < i:
        largest_num = i
    print(largest_num,i)
print(f"The largest number is {largest_num}")