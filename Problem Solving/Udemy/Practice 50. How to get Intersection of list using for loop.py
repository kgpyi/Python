x = [6, 8, 9, 10, [3, 6, 4], "t", "tt", "u", 1]
y = [1, 2, 3, 4, [3, 6, 4], 4, "tt"]

z = []

for i in x:
    for j in y:
        if i == j:
            z.append(i)

print(z)

