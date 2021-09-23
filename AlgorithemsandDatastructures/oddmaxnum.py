max = int(input("enter a max number"))
odd_numbers = []

for i in range(max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("odd numbers are", odd_numbers)
