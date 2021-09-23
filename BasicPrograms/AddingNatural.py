n = int(input("enter the number   :  "))
if n < 0:
    print("it is a negative number")
else:
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    print(sum)
