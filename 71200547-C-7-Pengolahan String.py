# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Latihan 7.2 Buatlah suatu program yang dapat menghitung frekuensi kemunculan suatu kata
yang ada pada String. Misal terdapat kalimat "Saya mau makan. Makan itu wajib. Mau siang
atau malam saya wajib makan". Ditanyakan kata "makan". Output: makan ada 3 buah
'''
'''
Input  : kalimat dan kata yang dicari dalam kalimat
Proses : ...
Output : 
'''

kalimat=str(input("Masukkan kalimat : "))
kata=str(input("Masukkan kata yang ingin dicari : "))
jumlah=0
kalimatlower=kalimat.lower()
katalower=kata.lower()

kata1=kalimatlower.count(katalower)
jumlah=jumlah+kata1
print("Kata",kata,"muncul",jumlah,"kali")
