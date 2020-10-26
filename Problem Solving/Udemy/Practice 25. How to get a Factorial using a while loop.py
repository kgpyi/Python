num = int(input("Enter the number you want to caculate factorial of: "))

mul = 1

while num > 0:
    mul = mul * num
    num -= 1

print("The factorial is:", mul)

