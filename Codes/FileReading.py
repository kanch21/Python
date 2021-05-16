# make sure the file you read sits in the current working directory
#opening  a file
#fopen = open(<filename>, <mode>)
#handle is something that can help you get the file but it itself is not a file.
#=========================
f = open("Sample.txt")
#method 1 for reading a file
print(f.read())

#method 2 for reading a file
# for i in f:
#     print(i)
f = open("Sample.txt")
count_lines = 0

#count the number of lines in a file
for line in f:
    count_lines = count_lines + 1
print('Line Count',count_lines)
#=========================

#=============================
#counting the chars in the file
f = open("Sample.txt")
fread = f.read()
print(fread)
print(len(fread))
#==============================

#=================================
#printing only selective lines
fhand = open('Sample.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)