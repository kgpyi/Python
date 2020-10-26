x = ["a", "b", "c", "d", "e"]
y = input("Inser an alphabet: ")

if y in x:
    print(y)
else:
    raise ValueError("Alphabet does not exist")

