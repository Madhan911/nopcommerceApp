# s = str(input(" enter a string  :  "))
#
# string = ""
# for i in s:
#     string = i + string
# print(s)
# print(string)
#

# s = "nanan"
#
# temp = s
# rev = s[-1::-1]
# print(s)
# print(rev)
#
# if temp == rev:
#     print(rev, "str is a palindrome")
# else:
#     print("not a palindrome string")


s = str(input("enter the string :  "))



string = ""

for i in s:
    string = i + string
print(string)

if s == string:
    print("it is a palindrome")
else:
    print("it is not a palindrime ")