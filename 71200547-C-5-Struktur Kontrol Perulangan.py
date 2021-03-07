# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah program Python untuk:
• Menghitung perkalian dua bilangan tanpa operator *
• Menghitung pemangkatan dua bilangan tanpa operator **
• Memeriksa apakah suatu bilangan adalah prima?
'''
'''
input  : angka & pengali, angka & pemangkat, angka
proses : ...
output : angka setelah dikali pengali, angka setelah dipangkatkan pemangkat, angka adalah bilangan prima atau bukan
'''

print("1. Perkalian")
print("2. Pemangkatan")
print("3. Menentukan bilangan prima")

hitung=str(input("Pilih penghitungan: "))

if hitung=="1":
    angka=int(input("Masukkan angka: "))
    pengali=int(input("Masukkan pengali: "))
    angka1=0
    for i in range (1,pengali+1):
        angka1=angka1+angka
    print(angka1)
elif hitung=="2":
    angka=int(input("Masukkan angka: "))
    pemangkat=int(input("Masukkan pemangkat: "))
    angka1=1
    for i in range (1,pemangkat+1):
        angka1=angka1*angka
        #angka=angka+angka
    print(angka1)
elif hitung=="3":
    angka=int(input("Masukkan angka: "))
    if angka>1:
        for i in range (2,angka):
            if angka%i==0:
                print(angka,"bukan bilangan prima")
                break
        else:
            print(angka,"adalah bilangan prima")
    else:
        print(angka,"bukan bilangan prima")