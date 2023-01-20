f = open("text18-19.txt.txt")
text = f.read()
f.close()
print("Содержимое файла:\n\n", text, sep="")
k = 0
for i in text:
    if i.isalpha():
        k += 1
print("\nКоличество букв:", k)
f = open("out.txt", "w")
f.write(text.lower())
f.close()