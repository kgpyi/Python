def isPalindrome(num):
    inital_num = num
    reverse = 0
    while num > 0:
        reverse = (reverse * 10) + (num % 10)
        num = int(num / 10)
    if reverse == inital_num:
        return True
    else:
        return False


def largest_palindrome(n):
    num1 = 10 ** n - 1
    num2 = 10 ** (n - 1)
    maxProduct = 0
    for i in range(num1, num2, -1):
        for j in range(num1, num2, -1):
            if isPalindrome(i * j) and i * j > maxProduct:
                maxProduct = i * j
    return maxProduct


print(largest_palindrome(3))
