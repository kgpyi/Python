exe = ["gif", "png", "jpeg", "jpg", "svg", "txt", "py"]

filexe = input("Insert file with extension: ").split(".")

if len(filexe) >= 2:
    Extension = filexe[-1].lower()
    if Extension in exe:
        print("File extenison known")
    else:
        print("Unkown file extension")

else:
    print("File doesnot have extension")

