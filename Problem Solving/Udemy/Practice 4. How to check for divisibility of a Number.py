num1, num2 = [float(x) for x in input("Enter numerator and denominator: ").split(" ")]
if num1 % num2 == 0:
    print("{} can divide {}", format(num2, num1))
else:
    print("{} cannot divide {}".format(num2, num1))

