# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
modul 6 soal latihan 6.3

Buatlah program untuk menampilkan deret seperti di bawah ini. n diinputkan secara dinamis
contoh: tinggi = 5, lebar = 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
'''
'''
Input  : tinggi dan lebar
Proses : ...
Output : ...
'''

tinggi=int(input("tinggi = "))
lebar=int(input("lebar = "))
nilai=1

for baris in range(1,tinggi+1):
    for kolom in range(1,lebar+1):
        print(nilai," ",end="")
        nilai=nilai+1
    print()