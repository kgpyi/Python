def sum_of_mult(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(sum_of_mult(1000))
