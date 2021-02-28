# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat menghitung damage multiplier pada skill hero dalam game jika melakukan critical hit!
Buat variabel yang dapat menerima tiga inputan, yaitu attack, critical damage, dan damage dealt!

keterangan :
- Attack berasal dari stats yang dimiliki oleh hero
- Critical damage adalah damage yang dikeluarkan jika hero melakukan critical hit, jika tidak ada tambahan crit damage maka crit damage = 150% (menggunakan tetapan cdmg default)
- Damage dealt berasal dari skill enhancement, jika skill enhancement mengatakan "+n% damage dealt" maka damage dealtnya 100% ditambah dengan skill enhancement (100% + n%)
- Buat kondisi dimana hero mendapatkan elemental advantage dan disadvantage. jika terdapat advantage maka damage dealt +40%, jika tidak ada advantage maka damage dealt *1. Penghitungan ini berdasarkan kondisi yang telah diinputkan oleh pengguna. 
- Jika serangan HIT maka damage*1, jika serangan MISS maka damage -25%. Penghitungan ini berdasarkan kondisi yang telah diinputkan oleh pengguna. 
'''
'''
Input  : attack=4100, crit damage=318%, damage dealt(skill 1)=+30%
Proses : ...
Output : damage total yang dikeluarkan
'''

#damage=atk*(cdmg/100)*dmgdealt

def damage(atk,cdmg=150,dmgdealt=1):
    adv=str.lower(input("elemental advantage(yes/no): "))
    if adv=="yes":
        damage=atk*(cdmg/100)*(dmgdealt+0.4)
    elif adv=="no":
        damage=atk*(cdmg/100)*dmgdealt
    hit=str.lower(input("hit/miss? "))
    if hit=="hit":
        damage=damage*1
    elif hit=="miss":
        damage=damage*0.75
    return int(damage)

print(damage(4100,318,1.3))