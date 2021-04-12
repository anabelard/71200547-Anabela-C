# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
anda adalah seorang programer. anda ditugaskan untuk membuat sebuah program untuk memasukkan data pada file "angka ganjil.txt" jika data tersebut merupakan angka ganjil. program akan menerima input dari pengguna dan program akan memasukkan bilangan ganjil antara angka 1 sampai dengan angka inputan tersebut. 
'''
'''
Input  : angka
Proses : ...
Output : isi dari file angka ganjil.txt (isi dari file datanya)
'''

angka=int(input("Masukkan angka: "))

createFile=open("angka ganjil.txt","w")
createFile.close()

for i in range(1,angka+1):
    for j in range(1,i):
        if i%2==0:
            break
    else:
        text="{} ".format(i)
        filetxt=open("angka ganjil.txt","a")
        filetxt.write(text)
        filetxt.close()

readFile=open("angka ganjil.txt","r")
read=readFile.read()
print(read)
readFile.close()