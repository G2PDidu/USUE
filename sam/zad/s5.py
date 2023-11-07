file = open("file.txt", "r")
content = file.read()

characters = len(content)
print("В файле", characters, "символов.")
file.close()