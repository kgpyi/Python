def fib(num):
    c = 0
    first = second = 1
    print(first, second, end=" ")
    while c < num - 2:
        nexti = first + second
        first = second
        second = nexti
        c += 1
        print(nexti, end=" ")


fib(10)

