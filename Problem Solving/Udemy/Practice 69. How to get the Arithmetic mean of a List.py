def avg_list(first):
    last = len(first)
    sum = 0
    for i in first:
        sum += i
    return sum / last


x = input("Insert some numbers").split(" ")

for i in range(len(x)):
    x[i] = float(x[i])

print(avg_list(x))

