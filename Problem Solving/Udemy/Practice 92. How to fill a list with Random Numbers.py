from random import randint

mini = int(input("Insert minimum number: "))
maxi = int(input("Insert maximum number: "))

y = int(input("Enter the range: "))
x = [randint(mini, maxi) for i in range(y)]

print(x)

