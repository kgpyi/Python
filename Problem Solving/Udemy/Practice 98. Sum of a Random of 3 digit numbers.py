from random import random

x = random() * 900 + 50
x = int(x)
print(x)

y = x // 100
z = (x // 10) % 10
w = x % 10

print(y + z + w)

