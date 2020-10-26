x = int(input("Enter the first number "))
y = int(input("Entre the second number "))


while x != 0 and y != 0:
    if x > y:
        x %= y
    elif y > x:
        y %= x

GCD = x + y

print("The Greatest Common Divisor is ", GCD)
