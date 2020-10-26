fp = open("C:/Users/khushal/Desktop/links.txt")
data = []

i = fp.readline()

while i != "":
    data.append(i)
    i = fp.readline()
fp.close()
print(data)
