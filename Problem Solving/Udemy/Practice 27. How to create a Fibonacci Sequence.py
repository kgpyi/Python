num = int(input("Enter the range: "))

f1 = f2 = 1
print(f1, f2, end=" ")
for y in range(num - 2):
    print(f1 + f2, end=" ")
    f1, f2 = f2, f1 + f2

