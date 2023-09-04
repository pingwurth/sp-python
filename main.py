def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    a = 3
    b = 4
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)