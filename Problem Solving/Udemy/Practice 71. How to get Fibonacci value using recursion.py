def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)


print(fib(10))
