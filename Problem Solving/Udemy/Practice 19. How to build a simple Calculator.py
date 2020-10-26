print("Enter 0 to end the life of this program: ")
while True:
    op = input("Enter the opreation (+, -, 4, /) ")
    if op == "0":
        break
    if op in ("+", "-", "*", "/"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if op == "+":
            print("Sum is %.2f" % (x + y))
        if op == "-":
            print("Minus is %.2f" % (x - y))
        if op == "*":
            print("Multipliaction is %.2f" % (x * y))
        if op == "/":
            print("Division is %.2f" % (x / y))
