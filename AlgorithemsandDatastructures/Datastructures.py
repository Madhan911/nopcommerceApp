def get_s_n(number):
    s_n = []
    for n in number:
        s_n.append(n * n)
    return s_n


number = [4, 8, 4, 6]
print(get_s_n(number))

