from random import randint

N = 30
array = []
for i in range(N):
    array.append(randint(1, 100))

array.sort()
print(array)

number = int(input("Enter the number you wish to search in array: "))

mini = 0
maxi = N - 1


while mini <= maxi:
    mid = (mini + maxi) // 2
    if number < array[mid]:
        maxi = mid - 1
    elif number > array[mid]:
        mini = mid + 1
    else:
        print("The number is loacted at index", mid)
        break
else:
    print("There is no such number")
