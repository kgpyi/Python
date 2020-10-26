num = int(input("Enter the number you wish to reverse "))

y = " "

while num > 0:
    x = num % 10
    y = y + str(x)
    num //= 10

print(y)
