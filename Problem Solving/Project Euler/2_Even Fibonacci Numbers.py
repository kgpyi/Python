def even_fib_sum(num):
    array = [1, 2]
    next_fib_num = 0
    while next_fib_num <= num:
        next_fib_num = array[(len(array) - 2)] + array[(len(array) - 1)]
        array.append(next_fib_num)
        sum = 0
    for even in array:

        if even % 2 == 0:
            sum += even
    return sum


print(even_fib_sum(4000000))
