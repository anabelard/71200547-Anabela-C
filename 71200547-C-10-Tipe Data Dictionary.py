# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah dictionary yang dapat menentukan tipe data dari data yang terdapat di dalam list apakah data tersebut termasuk tipe data huruf atau angka
'''
'''
Input  : list yang berisi data huruf maupun angka
Proses : ...
Output : dictionary yang berisi data dan tipe datanya
'''

def dataType(chara):
    d=dict() #d={}
    for i in chara:
        tipe=type(i)
        if tipe==str:
            d[i]="String"
        elif tipe==int:
            d[i]="Integer"
    return d

test=["xyz",89,995,"65",65]
print(dataType(test))