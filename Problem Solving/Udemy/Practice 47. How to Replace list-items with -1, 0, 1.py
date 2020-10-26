listitem = [6, 4, 5, 2, 1, 0, -5, -7, 0, -3, 2, -8, 4, -9, 0]

print(listitem)

for i in range(len(listitem)):
    if listitem[i] > 0:
        listitem[i] = 1
    elif listitem[i] < 0:
        listitem[i] = -1
    elif listitem[i] == 0:
        listitem[i] = 0

print(listitem)
