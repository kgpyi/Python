"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum"""


def sum_square_diff(n):
    sum_of_squares = int((n) * (n + 1) * (2 * n + 1) / 6)
    sum_of_nums = int((n) * (n + 1) / 2)
    square_of_sum = sum_of_nums * sum_of_nums
    diff = square_of_sum - sum_of_squares
    return diff


num = int(input())
print(sum_square_diff(num))
