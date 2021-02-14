# Nama : Anabela Rosanti Dewi Pramono
# Universitas Kristen Duta Wacana

'''
anda adalah seorang programer dalam sebuah game. anda ditugaskan untuk membuat program yang dapat mengkalkulasi stats akhir 
sebuah karakter setelah mencapai level maksimum dan diberi equipment. kegunaan equipment adalah menambah stats karakter 
dalam game yang berupa attack, defense, dan health. buatlah sebuah program untuk menghitung stats berbagai karakter yang 
sudah mencapai level maksimum setelah mengenakan equipment dan artifact jika base stats (attack, defense, dan health) tiap 
karakternya berbeda-beda! 

keterangan : 
- equipment yang digunakan adalah kombinasi antara atk set (menambah attack sebesar 35%) dan health set (menambah health sebesar 15%)
- artifact yang digunakan memberi tambahan stat sebanyak 273 attack dan 416 health

stats equipment yang digunakan adalah : 
- weapon   = +500 attack
- helmet   = +2700 health
- armor    = +300 defense
- boots    = +65% base health
- ring     = +65% base attack
- necklace = +65% base defense
'''

'''
input  : base attack = 1158, base defense = 553, base health = 6002
proses : ...
output : jumlah total stats karakter setelah diberi equipment dalam bilangan bulat
'''

#base stats
baseAtk=1158 #atk
baseDef=553 #def
baseHP=6002 #hp

#equipment
weapon=500 #atk
helmet=2700 #hp
armor=300 #def
boots=(65/100)*baseHP
ring=(65/100)*baseAtk
necklace=(65/100)*baseDef

#sets
setAtk=(35/100)*baseAtk
setHP=(15/100)*baseHP

#artifact
afAtk=273 #atk
afHP=416 #hp

#stats total
Atk=baseAtk+weapon+ring+setAtk+afAtk
Def=baseDef+armor+necklace
HP=baseHP+helmet+boots+setHP+afHP

#output
print("Attack = ",int(Atk))
print("Defense = ",int(Def))
print("Health = ",int(HP))
