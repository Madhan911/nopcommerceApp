
number = float(input("enter a number :  "))

if number > 0:
    print("it is a possitive number", number)
elif number == 0:
    print("it is equal to zero")
else:
    print("{0} is a negative number".format(number))