x = input('masukkan teks: ')
y = input('masukkan huruf pengganti vokal: ')
vokal = ['a','i','u','e','o'] 

for i in x:
    if i.lower() in vokal:
        print(y, end="")
    else:
        print(i,end="")


