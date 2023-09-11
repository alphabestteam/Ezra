file = open(r"Ezra\File Handling\3_first_text.txt", "r+")
print(file.read())

file.write("I've just accessed you through the write function :)")
print(file.read())
file.close()



