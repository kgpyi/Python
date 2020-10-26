import math

x1 = int(input("Insert the value of x1: "))
x2 = int(input("Insert the value of x2: "))
y1 = int(input("Insert the value of y1: "))
y2 = int(input("Insert the value of y2: "))
z1 = int(input("Insert the value of z1: "))
z2 = int(input("Insert the value of z2: "))

x = range(x1, x2 + 1)
y = range(y1, y2 + 1)
z = range(z1, z2 + 1)

for i in x:
    if i == 0:
        continue
    for j in y:
        for k in z:
            print(i, j, k, end=" ")
            A = j * j - 4 * i * k
            if A >= 0:
                x1 = (-j - math.sqrt(A)) / (2 * i)
                x2 = (-j + math.sqrt(A)) / (2 * i)
                print("Valid", x1, x2)
            else:
                x1 = complex((-j) / (2 * i), (math.sqrt(-A)) / (2 * i))
                x2 = complex((-j) / (2 * i), -(math.sqrt(-A)) / (2 * i))
                print("Complex roots", x1, x2)
