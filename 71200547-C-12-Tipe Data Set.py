# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat menghitung gabungan (u) dan irisan (n) dari dua himpunan. 
'''
'''
Input  : himpunan 1 dan himpunan 2
Proses : ...
Output : AnB atau AuB
'''

A=set()
B=set()

jumlahA=int(input("Jumlah anggota himpunan A : "))
for i in range(jumlahA):
    insertA=int(input("Masukkan bilangan : "))
    A.add(insertA)

jumlahB=int(input("Jumlah anggota himpunan B : "))
for j in range(jumlahB):
    insertB=int(input("Masukkan bilangan : "))
    B.add(insertB)

print("Pilih operasi yang diinginkan")
print("1. AuB")
print("2. AnB")
print("3. exit")
c=str(input("Masukkan pilihan : "))
while c=="1" or "2":
    if c=="1":
        print(A|B)
        print("Pilih operasi yang diinginkan")
        print("1. AuB")
        print("2. AnB")
        print("3. exit")
        c=str(input("Masukkan pilihan : "))
    elif c=="2":
        print(A&B)
        print("Pilih operasi yang diinginkan")
        print("1. AuB")
        print("2. AnB")
        print("3. exit")
        c=str(input("Masukkan pilihan : "))
    elif c=="3":
        print()
        break
    else:
        print("invalid input")
        print("Pilih operasi yang diinginkan")
        print("1. AuB")
        print("2. AnB")
        print("3. exit")
        c=str(input("Masukkan pilihan : "))
else:
    if c=="3":
        exit
    else:
        print("invalid input")
        print("Pilih operasi yang diinginkan")
        print("1. AuB")
        print("2. AnB")
        print("3. exit")
        c=str(input("Masukkan pilihan : "))