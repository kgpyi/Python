str = input("Insert a string: ")

lenstr = len(str)

for i in range(lenstr // 2):
    if str[i] != str[-1 - i]:
        print("This is not a Palindrome")
        quit()

print("This is a Palindrome!")
