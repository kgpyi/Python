fp = open("C:/Users/khushal/Desktop/links2.txt", "w")

fp.write("Hello World \n")
fp.write("Hello world 2\n")

fp.writelines("Hello World 3")

text = ["Hello Word 4 \n", "Hello World 5\n"]
fp.writelines(text)
fp.close()

fp = open("C:/Users/khushal/Desktop/links2.txt")
print(fp.read())
fp.close()

