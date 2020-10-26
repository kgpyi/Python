x = int(input("enter the nth element: "))

f1 = f2 = 1
y = 2
while y < x:
    f1, f2 = f2, f1 + f2
    y += 1
print(f2)
