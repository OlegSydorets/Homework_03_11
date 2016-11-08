i = [-1, 0, 1, 2, 3, 4, 5]
print(max(i))
print(min(i))

i = list(range(100))[::2]
print(i)

i = list(range(100))[1::2]
print(i)


i = float(input('Введите число X: '))
if i % 2 == 0:
    print("Четное".format(i))
else:
    print('Нечетное'.format(i))

for x in range(1, 10):
    for y in range(1, 10):
        print('{0} x {1} = {2}'.format(x, y, x*y))


n = 10
for i in range(1, n + 1):
    print('*' * i)

n = 6
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

print(sum(map(int, input().split())))


def summa(a):
    a = a.split()
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)


s = 0
while 1:
    a = input()
    if a == '_':
        break
    s += summa(a)
    print('Summa:', s)

i = 1
lens = ['poi', 'asdffghj', 'hj', 'oiiiiiiiiiiiii']

while i < len(lens):
    if len(lens[i]) >= 5:
        del lens[i]
        continue
    i = i + 1
print(lens)

a = [1, 2, 3], [4, 5, 6], [7, 8, 9]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()
