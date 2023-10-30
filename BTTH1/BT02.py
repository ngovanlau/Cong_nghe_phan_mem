n = int(input('n = '))

# a = []
# for i in range(n):
#     a.append(int(input(f"a[{i}] = ")))
# print(a)

a = [int(input(f"a[{i}] = ")) for i in range(n)]

duong = [x for x in a if x > 0]
if len(duong) == 0:
    print('So duong lon nhat: *')
else:
    print(f'So duong lon nhat: {max(duong)}')

am = [x for x in a if x < 0]
if len(am) == 0:
    print('So am nho nhat: *')
else:
    print(f'So am nho nhat: {min(am)}')

for x in set(a):
    print(f'{x} xuat hien {a.count(x)} lan')

k = int(input('k = '))
kq = [x for x in set(a) if a.count(x) == k]
print(kq)

a.sort(reverse=True)
print(a)