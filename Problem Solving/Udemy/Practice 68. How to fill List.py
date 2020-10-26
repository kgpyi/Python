from random import randint


def list_fill(first, qty, mini, maxi):
    for i in range(qty):
        first.append(randint(mini, maxi))
    return first


minimum = int(input("Enter minimum value: "))
maximum = int(input("Enter maxmium value: "))
num = int(input("Enter the number of elements: "))

x = []

print(list_fill(x, num, minimum, maximum))

