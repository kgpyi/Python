from random import randint

row = 5
col = 10
matrix = []

for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(randint(1, 100))
    matrix.append(myrow)

for i in matrix:
    print(i)

num = int(input("range of number(1-100): "))

for j in range(col):
    for i in range(row):
        if matrix[i][j] == num:
            print("Row number is {} and coloum number is {}".format(i, j))

print()
