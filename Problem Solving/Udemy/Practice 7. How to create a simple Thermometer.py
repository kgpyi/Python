x = input("Enter the temperature in Celsius or Fahrenheit ")

unit = x[-1]
print(unit)
num1 = float(x[0:-1])

if unit == "C" or unit == "c":
    num1 = num1 * (9 / 5) + 32
    print("The temperature in Farhrenheit is {} F".format(num1))

elif unit == "F" or unit == "f":
    num1 = (num1 - 32) * (5 / 9)
    print("The temperature in Celsius is {} C".format(num1))

else:
    print("Not correct format")
