from random import random

num = 2000
listitem = [0] * num

for i in range(num):
    listitem[i] = int(random() * 100)

print(listitem)

maxi = 1
leng = 1
code = 0

for i in range(1, num):
    if listitem[i] > listitem[i - 1]:
        leng += 1
    else:
        if leng > maxi:
            maxi = leng
            code = i
        leng = 1

print("The maxmium length = ", maxi)
print("The ordered values are = ", listitem[code - maxi : code])

