# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("normal = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZZZzZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + "is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# # isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_star = "Sangjaangnim Oppa".startswith("Sangjangnim")
print("star = " + str(cek_star))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_judul))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

# alokasi karakter rjust(), ijust() center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("=") # ini adalah menghilangkan tanda =
print("'"+tengah+"'")