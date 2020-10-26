goods = {}

for i in open("C:/Users/khushal/Desktop/links2.txt"):
    cate = i.split()
    cate[1] = float(cate[1])
    cate[2] = int(cate[2])
    goods[cate[0]] = cate[1:]


print(goods)

