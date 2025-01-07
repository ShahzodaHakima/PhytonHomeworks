text=input("matnni kiriting: ")
words=text.split()
a=""
for word in words:
    a=a + word[0].upper()
print(a)
