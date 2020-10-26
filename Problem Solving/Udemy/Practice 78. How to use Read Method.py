fp = open("C:/Users/khushal/Desktop/links.txt")
data = fp.read()
fp.close()

print(repr(data))

data = data.split("\n")
print(data)

