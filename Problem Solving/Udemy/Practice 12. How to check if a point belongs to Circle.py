x, y = [float(num) for num in input("Enter the x and y cooridantes: ").split(",")]
r = float(input("Enter the radius: "))

Distance = (x ** 2) + (y ** 2)
Distance = Distance ** 0.5
if Distance > r:
    print(" {},{} lie outside the circle".format(x, y))

elif Distance == r:
    print("{},{} lie on the circle".format(x, y))

elif Distance < r:
    print("{},{} lie inside the circle".format(x, y))

