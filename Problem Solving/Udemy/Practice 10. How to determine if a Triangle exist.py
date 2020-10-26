num1, num2, num3 = [float(x) for x in input("Entre the side of tirangle ").split(" ")]

if num1 < num2 + num3 or num2 < num1 + num3 or num3 < num1 + num2:
    print("Triangle can exit")
else:
    print("Triangle cannot exit")
