from random import randint

row = 6
col = 12

x = []

for i in range(row):
    y = []
    for j in range(col):
        y.append(randint(1, 10))
    x.append(y)

for i in x:
    for j in i:
        print("%2d" % j, end=" ")
    print()

