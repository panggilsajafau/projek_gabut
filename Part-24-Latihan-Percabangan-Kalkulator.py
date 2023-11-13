# Latihan

# kalkulator sederhana
print(20*"=")
print("Kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 = "))

# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
elif operator == "x":
    hasil = angka_1 * angka_2
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")

print("Akhir dari program, terima kasih")