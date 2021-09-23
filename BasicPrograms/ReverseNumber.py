# n = 233
#
# rev_num = 0
# while n > 0:
#     rev_num= rev_num * 10 + n % 10
#     n = n // 10
#
# print(rev_num)


# n = int(input("enter a number   :  "))
#
# temp = n
# rev_num = 0
# while temp > 0:
#     rev_num = rev_num * 10 + temp % 10
#     temp = temp // 10
#
# print(rev_num)
#
# if n == rev_num:
#     print("it is a palindrome number")
# else:
#     print("not a palindrome")


n = int(input("enter the number  :  "))

temp = n
rev_num = 0

while temp > 0:
    rev_num = rev_num * 10 + temp % 10
    temp = temp // 10

print(rev_num)
if n == rev_num:
    print("it is palindrome number")
else:
    print("it is not palindrime number")