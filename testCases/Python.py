'''
m = input('enter first number')
n = input('second number')

plus = float(m)+float(n)
print("the sum of {0} and {1} is {2}".format(m, n, plus))
'''

'''
#area of triangle
a = float(input("enter first side"))
b = float(input("enter second  side"))
c = float(input("enter third side"))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c) ** 0.5)

print('The area of the triangle is %0.2f' %area)
'''
'''

#quartedic eqation
import cmath

a = float(input("enter the number a:"))
b = float(input("enter the number b:"))
c = float(input("enter the number c:"))

d = (b ** 2) - (4 * a * c)

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("the values are {0} and {1} ".format(sol1,sol2))

'''


