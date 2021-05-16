#Basics
str1 = "Kanchan"
str2 = "Chowdhari"
result = str1 + ' ' + str2
print(result)

#if a variable contains a number in the string format, and you want to typecast it to int, one can do so using int()
str3 = '25'
str4 = '20'
result2 = int(str3) + int(str3)   #just like this!
print(result2)

#iterating through the whole string one by one!
j = 0
for j in range(0, len(str1)):
    letter = str1[j]
    print(letter, j)


#we can find letters from the string using index. the index value always starts with 0.
letter=str1[3]
print(letter)

#Note- you will get an error like string index out of range if you try to access an index value beyond the end of string

#compute the length of string using len()
print(len(str1))

#counting the letter 'i' in a string

str5 = input('enter a string')
count = 0
for i in str5:
    if i == 'h':
        count += 1
print(f"count of letter h is {count}")

#slicing the string

string = 'Kanchan Chowdhari'
print(string[ 0 : 4])
#note- the second number after : is the num uptil which the values are displayed. ie "up to but not including"

# assuming first of string
print(string[ : 4])

#assuming last of string
print(string[5: ])

#taking the whole string
print(string[ : ])

#using 'in' as a logical operator
if 'a' in string:
    print('found it!')

#string comparison
word = 'bamboos'
if word < 'ake':
    print(f"{word} comes before cake")
elif word == 'bamboos':
    print("both the words are same!")

#String library- string functions

lower_str = string.lower()
upper_str = string.upper()

print(f"the lower case of string is {lower_str}")
print(f"the upper case of string is {upper_str}")

#find()- finds the first occurrence of the string. if find() does not get the string to be searched, it returns -1
#here string= "Kanchan Chowdhari"
pos = string.find('ab')
print(pos)

#replace()- this is like search and replace
#replace('search string','replacement string')
#use case 1
string = string.replace('Chowdhari','Sharma')
print(f'the replaced name is {string}')

#use case 2
string2 = string.replace('a','o')
print(f" the replaced name is {string2}")

#stripping whitespaces
#lstrip()- strips whitespaces from left
#rstrip()-  strips whitespaces from right
#strip()- strips whitespaces from both left and right
str6 = '    Hello    World    '
res_lstrip = str6.lstrip()
res_rstrip = str6.rstrip()
res_strip = str6.strip()

print(f" lstrip string is {res_lstrip} \n rstrip string is {res_rstrip} \n strip string is {res_strip}")

# dir() returns all the lsit of attributes and methods that can be used for the string variable
print(dir(string))


#use case 2
data = 'From jamie.lanister@uct.ca.za Sat Jan 05 09:14:16 2021'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos) #here its trying to find the first occurence of space after atpos position.

print(data[atpos + 1 : sppos])
