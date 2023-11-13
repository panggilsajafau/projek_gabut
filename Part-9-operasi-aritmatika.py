# Operasi Aritmatika
print('==========Operasi Aritmatika=========')
a = 10
b = 3

#Operasi Tambah +
print('==========Operasi Tambah==========')
hasil = a + b
print(a, '+' ,b, '=', hasil)

#Operasi Pengurangan -
print('==========Operasi Pengurangan==========')

hasil = a - b
print(a, '-' ,b, '=', hasil)

#Operasi Perkalian * 
print('==========Operasi Perkalian==========')
hasil = a * b
print(a, '*' ,b, '=', hasil)

#Operasi Pembagian /
print('==========Operasi Pembagian==========')
hasil = a / b
print(a, '/' ,b, '=', hasil)

#Operasi Eksponen (Pangkat) **
print('==========Operasi Eksponen (Perangkat)==========')
hasil = a ** b
print(a, '**' ,b, '=', hasil)

#Operasi Modulus %
print('==========Operasi Modulus==========')
hasil = a % b
print(a, '%' ,b, '=', hasil)

#Operasi Floor division //
print('==========Operasi Floor division==========')
hasil = a // b
print(a, '//' ,b, '=', hasil)

#Prioritas Operasi, operation precedence
'''
    1. ()
    2. Exponen **
    3. Perkalian dan teman teman * / ** % //
    4. Pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y -y % z // x
print(x, '**', y, '*',z, '+', x, '/', y, '-', y, '%', z, '//', x, '=',hasil)

hasil = x + y * z
print(x, '+',y,'*',z,'=',hasil)
# Kurung akan mengambil langkah paling awal
hasil = (x + y) * z
print('(',x, '+',y,')*',z,'=',hasil)