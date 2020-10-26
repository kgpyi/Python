num = int(input("Enter the number you wish to convert: "))
base = int(input("Enter the base (2-9): "))

if base > 9 or base < 2:
    print("Enter vaild base: ")

num2 = " "
while num > 0:
    num2 = str(num % base) + num2
    num //= base

print(num2)
