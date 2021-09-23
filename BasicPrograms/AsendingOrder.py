
#In programming, a flag is a predefined bit or bit sequence that holds a binary value. Typically, a program uses a flag to remember something or to leave a sign for another program.


list_one = [1,2,3]

flag = 0
if list_one == sorted(list_one):
    flag = 1

if flag:
    print("list is sorted")
else:
    print("list is not sorted")



'''
list_one = [1, 2, 3]
flag = 0
i = 1

while i < len(list_one):
    if list_one[i] < list_one[i - 1]:
        flag = 1
    i += 1
if flag:
    print(list_one, "is not sorted")

else:
    print(list_one, "is  sorted")


'''

list_one = [1, 2, 3]
flag = 0

list_two = list_one[:]
list_two.sort()
if [list_one == list_two]:
    flag = 1

if flag:
    print(list_one, "is  sorted")

else:
    print(list_one, "is  not sorted")

