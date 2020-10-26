str = input("Enter any string with upper and lowercase ")

lenstr = len(str)

upper = lower = 0


for i in str:
    if "a" <= i <= "z":
        lower += 1
    elif "A" <= i <= "Z":
        upper += 1

print("Percentange of Uppercase: %.2f %%" % (upper / lenstr * 100))
print("Percentange of Lowercase: %.2f %%" % (lower / lenstr * 100))

