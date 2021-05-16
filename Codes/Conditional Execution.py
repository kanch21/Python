# #Two way condition
# x = 1
# if x > 5:
#     print("Larger")
# else:
#     print("Smaller")
# print("out of condition")
#
# #nested if
# x = 2
# if x <= 100:
#     print(f'{x} is less than 100')
#     if x < 5:
#         print(f'{x} is smaller even!')
#     print('end of inner if')
# print('end of outer if')



#Multi-way- in this way, on,ly one condition works at a time.
x = 1
if x > 5 and x<=10:
    print("mid sized number")
elif x>0 and x<=5:
    print("small sized number")
else:
    print("large sized number")
print("end of condition")

#no else- if no condition satisfies, the last print statement executes.
x = 20
if x>0 and x<=5:
    print("small sized number")
elif x > 5 and x<=10:
    print("mid sized number")
elif x > 10:
    print("large sized number")

print("end of condition")

