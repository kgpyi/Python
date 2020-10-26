# Nth_Fibonacci
# Problem Statement
# The Fibonacci sequence is dened as follows: the first number of the sequence is 0, the second number is 1,
# and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
# Write a function that takes in an integer n and returns the nth Fibonacci number.

# Sample input: 6

# Sample output: 5 (0, 1, 1, 2, 3, 5)


# Method 1 - Using Recussion


def get_Nth_Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_Nth_Fibonacci(n - 1) + get_Nth_Fibonacci(n - 2)


# Time Complexity - O(2^n)   Space Complexity - O(n)


# Method 2 - Using Memoization


def get_Nth_Fibonacci(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_Nth_Fibonacci(n - 1, memoize) + get_Nth_Fibonacci(
            n - 2, memoize
        )
        return memoize[n]


# Time Complexity - O(n)     Space Complexity - O(n)


# Method 3 - Iteration


def get_Nth_Fibonacci(n):
    last_Two = [0, 1]
    counter = 3
    while counter <= n:
        next_One = last_Two[0] + last_Two[1]
        last_Two[0] = last_Two[1]
        last_Two[1] = next_One
        counter += 1
    if n > 1:
        return last_Two[1]
    else:
        return last_Two[0]


# Time Complexity - O(n)     Space Complexity - O(1)
