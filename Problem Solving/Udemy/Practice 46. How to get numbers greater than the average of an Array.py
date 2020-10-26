import random

x = []

for i in range(20):
    x.append(random.random() * 100)

print(x)
avg = 0

for i in range(20):
    avg = avg + x[i]


avg = avg / 20
print("Average is", avg)
for i in range(20):
    if x[i] > avg:
        print(x[i])

