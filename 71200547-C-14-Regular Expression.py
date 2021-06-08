# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Sebuah tabel menampilkan data yang diurutkan berdasarkan abjad. Buatlah agar data pada tabel diurutkan berdasarkan nilainya!

Nama   | Nilai
_______|_______
Andi   | 95 
Budi   | 78 
Caca   | 90 
Doni   | 100 
Evan   | 87 
'''
'''
Input  : string nama dan nilai
Proses : ...
Output : tabel data yang diurutkan berdasarkan nilai
'''

import re
jumlahData=int(input("Masukkan jumlah data: "))
Data=""
for i in range(1,jumlahData+1):
    DataKeI=input(("Masukkan Data ke-{}: ").format(i))
    Data=Data+DataKeI

nama=re.findall("[a-zA-Z]+",Data)
nilai=re.findall("[0-9]+",Data)

lstNilai=[]
lstNilaiSorted=[]

for j in nilai:
    j=int(j)
    lstNilai.append(j)
    lstNilaiSorted.append(j)

lstNilaiSorted.sort()
lstNilaiSorted.reverse()

d=dict()

for k in lstNilaiSorted:
    index=lstNilai.index(k)
    d[nama[index]]=lstNilai[index]

print("Nama    | Nilai")
print("-----------------")
for l in d:
    print(l,"   |",d[l])