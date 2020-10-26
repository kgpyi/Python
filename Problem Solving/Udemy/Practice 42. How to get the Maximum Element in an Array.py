from random import randint

x = 20
array = []

for i in range(x):
    array.append(randint(1, 1000))

print(array)
max = 0

for i in array:
    if i > max:
        max = i

print(max)
