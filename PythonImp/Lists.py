list = ["nani", "nani","chinnu", "madhan", 1, 0.11, 0+5j, "nn"]

list1 = [1,3,5]

tuple = (8, 9, 10)
print(list[0])

print(list[-1])

print(list[2:5])

print(list[:4])

print(list[4:])

'''list[1] = "chinni"
print(list) 

list1[0:2] = ["chinni", "rama"]
print(list1) 

list1.insert(3, 6)
print(list1)    '''

#adding operations
list1.append(7)
print(list1)

list.extend(list1)
print(list)

list1.extend(tuple)
print(list1)

#remove operations

list1.remove(10)
print(list1)

list1.pop(0)
print(list1)


del list1[0]
print(list1)

#list1.clear()
#print(list1)

for i in list1:
    print(i)


list2 = [1,33,55,88]
for i in range(len(list2)):
    print(i)

i = 0
while i < len(list2):
    print(i)
    i = i + 1


list3 = ["nani","madhan","chinni"]
list4 = []

for x in list3:
    if "a" in x:
        list4.append(x)
print(list4)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

mylist = thislist.copy()
print(mylist[0])


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for i in list2:
    list1.append(i)

print(list1)

