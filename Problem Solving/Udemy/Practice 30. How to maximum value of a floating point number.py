from random import random

num = round(random() * 1000, 3)
print(num)

y = str(num)
maxi = -1

for i in range(len(y)):
    if y[i] == ".":
        continue
    elif maxi < int(y[i]):
        maxi = int(y[i])
print("The maximun number is ", maxi)
