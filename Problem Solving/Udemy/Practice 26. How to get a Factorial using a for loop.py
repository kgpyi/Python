x = int(input("Enter the number you want to caculate Factorial of: "))

mul = 1
for i in range(2, x + 1):
    mul = mul * i


print("The factorial is:", mul)
