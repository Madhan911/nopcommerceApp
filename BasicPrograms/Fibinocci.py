# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# n = int(input("enter the number :  "))
# a = 0
# b = 1
# if n < 0:
#     print("it is a negative number ")
# elif n == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# def feb(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("it is a negative number")
#     elif n == 1:
#         print(a)
#     elif n == 2:
#         print(a)
#         print(b)
#     else:
#         print(a)
#         print(b)
#
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
#
#
# feb(10)


def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


# create generator object

for i in fib(10):
    print(i)
