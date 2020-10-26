x = input("What do you want to caculate out of Mass, Denisty and Volume?, Enter(m,d,v)")

if x == "m":
    d = float(input("Enter value of Denisty "))
    v = float(input("Enter value of Volume "))
    num = d * v
    print("Mass is ", num)

if x == "v":
    d = float(input("Enter value of Denisty "))
    m = float(input("Enter value of Mass "))
    num = m / d
    print("Volume is ", num)

if x == "d":
    m = float(input("Enter value of Mass "))
    v = float(input("Enter value of Volume "))
    num = m / v
    print("Denisty is ", num)

