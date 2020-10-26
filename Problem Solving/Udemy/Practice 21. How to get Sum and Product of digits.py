num = int(input("Enter the numner: "))
add = 0
mul = 1

while num > 0:
    add += num % 10
    mul *= num % 10
    num //= 10

print(add)
print(mul)

