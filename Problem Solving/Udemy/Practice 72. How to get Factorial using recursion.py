def fact(num):
    if num == 1:
        return num
    return num * fact(num - 1)


num = int(input("Entre the number you want to calcualte factorial of: "))
print(fact(num))

