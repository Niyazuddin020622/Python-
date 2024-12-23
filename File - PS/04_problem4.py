word = "Donkey"

with open("File - PS/file.txt","r")as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("File - PS/file.txt","w") as f:
    f.write(contentNew)