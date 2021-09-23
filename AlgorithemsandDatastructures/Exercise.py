'''
exp = [1200, 2000, 5000, 555, 4777, 4444, 2121]

print("substraction from feb to jan is ", exp[1] - exp[0])

print(" total expenses of 3 months ", exp[1] + exp[0] + exp[2])

print(" did i spend 2000 dollers in ", 2000 in exp)

exp.append(55551)
print(exp)
exp[0] = exp[0] - 200
print(exp)
'''

heros = ['spider man', 'thor', 'hulk', 'black panther', 'iron man', 'captain america']

print(len(heros))

heros.remove('black panther')
heros.insert(3, 'black panther')

heros[3] = "blackpanther"

print(heros)

heros.append("blackpanther")
print(heros)

heros[1:3] =['doctor strange']
print(heros)
heros.sort()
print(heros)

