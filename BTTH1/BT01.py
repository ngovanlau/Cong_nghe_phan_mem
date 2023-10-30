n = int(input("n = "))

print(("*" * n + "\n") * 5)

print('\n')
for i in range(1, n + 1):
    print('*' * i)

print('\n')
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

print('\n')
for i in range(1, n + 1, 2):
    print(('*' * i).center(n))