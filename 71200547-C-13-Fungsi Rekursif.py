# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
buatlah fungsi untuk mengalikan dan membagi dua buah bilangan dengan metode rekursif
'''
'''
Input  : a dan b
Proses : ...
Output : ...
'''

def kali(a,b):
    if b>0:
        return a+kali(a,b-1)
    else:
        return 0

def bagi(a,b):
    if a-b==0:
        return 1
    else:
        return 1+bagi(a-b,b)

print(kali(2,10))
print(bagi(10,5))