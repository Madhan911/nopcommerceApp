def fact(n):
    return 1 if (n == 0 or n == 1) else n * fact(n - 1)


num = 3

print("Factorial of", num, "is", fact(num))

'''
num = int(input("enter the number :  "))

factorial = 1

if num < 0:
    print("number is a negative number")
elif num ==0:
    print("factorial number one is 0 ")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("the factorial of ", num, "is ", factorial)


'''
