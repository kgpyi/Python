# for series = 1,-0.5,0.25,-0.125


x = int(input("Enter the number of elements in series: "))


total = 0
z = 0
y = 1
while z < x:
    total = total + y
    y /= -2
    z += 1

print(total)
