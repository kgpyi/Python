from random import randint

row = 5
col = 5
matrix = []

for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(randint(1, 9))
    matrix.append(myrow)

for myrow in matrix:
    print(myrow)

sum_diag1 = 0
sum_diag2 = 0

for i in range(row):
    sum_diag1 += matrix[i][i]
    sum_diag2 += matrix[i][row - i - 1]

print(sum_diag1)
print(sum_diag2)
