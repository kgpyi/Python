import math

num = int(input("Enter the number to check: "))

if num < 2:
    print("Please, insert numver greater than 2")
    quit()
elif num == 2:
    print("This is a prime nymber")


y = 2
x = int(math.sqrt(num))
while y <= x:
    if num % y == 0:
        print("This is a complex number")
        quit()
    y += 1

print("This is a prime number")

