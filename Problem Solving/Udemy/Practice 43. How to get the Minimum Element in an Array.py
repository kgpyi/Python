from random import randint

x = 20
array = []

for i in range(x):
    array.append(randint(1, 1000))

print(array)
min = array[0]

for i in array:
    if i < min:
        min = i

print(min)
