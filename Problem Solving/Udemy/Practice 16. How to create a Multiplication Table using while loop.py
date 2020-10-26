num1 = 1

while num1 <= 10:
    num2 = 1
    while num2 <= 10:
        print("%4d" % (num1 * num2), end=" ")
        num2 += 1
    print()
    num1 += 1

