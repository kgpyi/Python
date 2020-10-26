import random

x = []

for i in range(100):
    x.append(int(random.random() * 20) - 10)

print(x)

pos = []
neg = []

for i in x:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print("Negtaive numbers = ", neg)
print("Postive numbers = ", pos)
