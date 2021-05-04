# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Sebuah tabel data nilai yang berisi kolom nama dan nilai telah dipisahkan per kolom menjadi sebuah tuple. Buatlah sebuah program yang dapat menyatukan data-data tuple tersebut menjadi tabel seperti semula! 
'''
'''
Input  : tuple nama dan tuple nilai
Proses : ...
Output : tabel nama dan nilai / tabel data nilai yang semula sebelum diubah menjadi tuple
'''

def daftarNilai(name,score):
    lstname=list(name)
    lstscore=list(score)
    capitalizedNames=[]
    for i in lstname:
        capitalizedName=i.upper()
        capitalizedNames.append(capitalizedName)
    print("Nama    | Nilai")
    print("="*15)
    for j in range(len(lstname)):
        print(("{}      | {}").format(capitalizedNames[j],lstscore[j]))

nama=("Aa","bB","cc","DD")
nilai=(100,90,95,87)
daftarNilai(nama,nilai)