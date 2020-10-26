num = int(input("Enter a number: "))

temp = 0

while num > 0:
    num = num // 10
    temp += 1
print(temp)
