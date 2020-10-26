def LCM(x, y):
    z = x * y

    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x

    return z // (x + y)


a = int(input("Insert first number: "))
b = int(input("Insert second number: "))

print("The LCM = ", LCM(a, b))

