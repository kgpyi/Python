x = int(input("Insert a number: "))

even = 0
odd = 0

while x > 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x //= 10

print("Even number = %d, Odd number %d" % (even, odd))
