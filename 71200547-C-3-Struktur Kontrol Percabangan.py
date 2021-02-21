# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat menampilkan jumlah hari dalam suatu bulan pada tahun tertentu berdasarkan input pengguna!

Ketentuan :
- pengguna diminta memasukkan tahun dan bulan
- jika input salah berarti input pengguna tidak valid
- perhatikan penghitungan jumlah hari juga termasuk tahun kabisat
- buat juga dalam bentuk ternary operator
'''
'''
input  : tahun dan bulan
proses : ...
output : jumlah hari dalam bulan yang diinput oleh pengguna
'''

tahun=int(input("Masukkan tahun:"))
bulan=int(input("Masukkan bulan (1-12):"))

if bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12 :
    print("Jumlah hari: 31")
elif bulan==4 or bulan==6 or bulan==9 or bulan==11 :
    print("Jumlah hari: 30")
elif bulan==2 :
    if tahun%4==0 :
        print("Jumlah hari: 29")
    elif tahun%4!=0 :
        print("Jumlah hari: 28")
else :
    print("Input tidak valid")

#ternary operator
tahun=int(input("Masukkan tahun:"))
bulan=int(input("Masukkan bulan (1-12):"))
print("Jumlah hari: 31") if bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12 else print("Jumlah hari: 30") if bulan==4 or bulan==6 or bulan==9 or bulan==11 else print("Jumlah hari: 29") if bulan==2 and tahun%4==0 else print("Jumlah hari: 28") if bulan==2 and tahun%4!=0 else print("Input tidak valid")
