num1, num2, num3 = [int(num) for num in input("Enter three value: ").split(" ")]
maxnum = num1

if maxnum < num2:
    maxnum = num2
if maxnum < num3:
    maxnum = num3
print(maxnum)
