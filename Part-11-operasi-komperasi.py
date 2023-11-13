# operasi komperas 

# setiap hasil dari komperasi komperasi adalah boolean

# >,<,>=,<=,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('==========Lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(a,'>',3,'=',hasil)
hasil = b > 2
print(a,'>',2,'=',hasil)

# lebih kecil dari <
print('==========Kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(a,'<',3,'=',hasil)
hasil = b < 2
print(a,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('==========Lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 2
print(a,'>=',2,'=',hasil)

# Kurang dari sama dengan >=
print('==========Kurang dari sama dengan (<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 2
print(a,'<=',2,'=',hasil)

# Sama dengan (==)
print('==========sama dengan (<=)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# Tidak sama dengan (!=)
print('==========tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi objek identity
print('==========object identity (is)')
x = 5 # ini adalah assignment membuat objek
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 # ini adalah assignment membuat objek
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)