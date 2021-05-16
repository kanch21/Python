#List is a type of collection
#It is surrounded by []
#it can be any python object, ie a list can have multiple datatypes
#default starting index is 0
#Lists are mutable

friends = ['Garima', 'Gargee', 'Isha']

#adding items in list
friends.append("Darshu")
friends.append("Isha")


print(friends[2])
#method 1
for friend in friends:
    print(f"{friend} is my close friend")
#method 2
for friend in range(len(friends)):
    print(f"{friends[friend]} is my close friend")

friends[2]='Aditi'
friends.sort()
print(friends)
# len() gives the count of items in the list
print(len(friends))

# concatenation of lists using +
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)
print(c[1:4])
#sorting the list
c.sort()
print(c)

#starting a list from scratch
stuff = list()
stuff.append(34)
stuff.append('Kanchu')
stuff.append('True')
print(stuff)
print('the length of stuff list is: ',len(stuff))

#computing average using list

numlist = list()

while True:
    inp = input("Enter a number:")
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('the average is :',average)


#STRING with LIST

sentence = 'Hey this is python'
words = sentence.split()  #the split function dividesthe sentence into words
print(words)
print(len(words))
print(words[2])
#note- the tab, space, whitespaces qualify in split()
for w in words:
    print(w)

#in order to split a sentence with delimiter other than spaces, you need to specify the delimiter in split()

line = 'alpha;beta;gamma;theta'
words2 = line.split()
print(words2)
#output - ['alpha;beta;gamma;theta']
#now we will add ; as the delimiter for splitting
words3 = line.split(';')
print(words3)
#output ['alpha', 'beta', 'gamma', 'theta']

#useful for real time cases where you want to extract the email id from the mail

email_info = 'LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Thu 5/13/2021 10:40 PM'
email_comp = email_info.split()
print(email_comp)
#['LinkedIn', 'Job', 'Alerts', '<jobalerts-noreply@linkedin.com>', 'Thu', '5/13/2021', '10:40', 'PM']
#we need to extract the email id
email_id = email_comp[3].rstrip('>').lstrip('<')
print(email_id)
#double split pattern
email_id_info = email_id.split('@')
print('host',email_id_info[1])