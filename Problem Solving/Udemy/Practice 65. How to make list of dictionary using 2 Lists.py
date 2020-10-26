x = ["a", "b", "c", "d"]
y = [1, 2, 3, 4]

z = {}
for i in range(len(x)):
    #    z[y[i]] = x[i]
    z = dict(zip(y, x))
print(z)
