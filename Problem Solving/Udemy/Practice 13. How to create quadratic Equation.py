from math import sqrt

x, y, z = [float(num) for num in input("Enter the value of x, y,z ").split(" ")]

cal = y * y - 4 * x * z

if cal > 0:
    root1 = (-y + sqrt(cal)) / (2 * x)
    root2 = (-y - sqrt(cal)) / (2 * x)
    print("root1 = {} \nroot2 = {}".format(root1, root2))

elif cal == 0:
    root = -y / (2 * x)
    print("roor is ", root)

else:
    root1 = complex((-y) / (2 * x), (sqrt(-cal)) / (2 * x))
    root2 = complex((-y) / (2 * x), -(sqrt(-cal)) / (2 * x))
    print("root1 = {} \nroot2 = {}".format(root1, root2))
