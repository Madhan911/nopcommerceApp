'''
number = int(input("enter the number :  "))

if number > 1:
    for i in range(2,number):
        if (number%i) == 0:
            print("{0} is not a prime number".format(number))
            break

    else:
        print("{0} is a prime number".format(number))
else:
    print("{0} is not a prime number".format(number))



lower = int(input("enter a lower number : "))
upper = int(input("enter a upper number : "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
'''

#number = int(input("enter a number  : "))


# def check_prime(num):
#     if num < 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# if check_prime(number):
#     print("number is prime ")
# else:
#     print("number is not a prime")

n = int(input("enter the value :   "))

if n >1:
    for i in range(2, n):
        if n%i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")
