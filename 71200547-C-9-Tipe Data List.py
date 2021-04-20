# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program untuk menginput data nama dan nilai siswa menggunakan list dan output berupa tabel nama dan nilai!
'''
'''
Input  : nama, nilai sebanyak jumlah nama dan nilai yang ingin dimasukkan
Proses : ...
Output : tabel nama dan nilai
'''

print("="*6,"INPUT DATA","="*6)
jumlah=int(input("Jumlah data yang ingin dimasukkan: "))

lstnama=[]
lstnilai=[]

for i in range(jumlah):
    nama=str(input("Masukkan nama: "))
    namacap=nama.capitalize()
    lstnama.append(namacap)
    nilai=int(input("Masukkan nilai: "))
    lstnilai.append(nilai)
    print("Data berhasil dimasukkan")

output=str(input("Print daftar?(ya/tidak) "))
output.lower()
if output=="ya":
    print()
    print("=====DAFTAR NILAI=====")
    print("Nama     Nilai")
    for j in range(jumlah):
        print(lstnama[j],"      ",lstnilai[j])
else:
    print("terimakasih") 
