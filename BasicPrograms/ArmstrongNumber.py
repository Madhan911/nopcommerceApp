'''

num = int(input("enter the number :  "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum+digit ** 3
    temp //= 10

if num == sum:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
'''

# low = int(input("enter the low number :  "))
# high = int(input("enter the high number :  "))
#
# for num in range (low, high+1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#         if num == sum:
#             print(num)


n = int(input("enter the number   :  "))

temp = n

sum = 0

while temp > 0:

    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if n == sum:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
