def find_lcm(num1, num2):
    if num1 > num2:
        num = num1
        den = num2
    elif num2 > num1:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = int(den)
    lcm = int((num1 * num2) / gcd)
    return lcm


n = int(input())
a = find_lcm(2, 3)
for i in range(4, n + 1):
    a = find_lcm(a, i)

print(a)
