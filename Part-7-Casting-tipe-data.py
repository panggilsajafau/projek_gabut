# Kita belajar Casting
# merubah dari suatu tipe ke tipe lain
# tipe data = int, float, str, bool

# int
print("=====int=====")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, ", type =",type(data_float))
print("data = ", data_str, ", type =",type(data_str))
print("data = ", data_bool, ", type =",type(data_bool))

## float
print("=====float=====")
data_float = 9.5;
print("data = ", data_float, ",type =",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data = ", data_int, ", type =",type(data_float))
print("data = ", data_str, ", type =",type(data_str))
print("data = ", data_bool, ", type =",type(data_bool))

## boolean
print("=====boolean=====")
data_bool = True;
print("data = ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan di bulatkan kebawah
print("data = ", data_int, ", type =",type(data_float))
print("data = ", data_str, ", type =",type(data_str))
print("data = ", data_float, ", type =",type(data_float))

## String
print("=====string=====")
data_bool = 10;
print("data = ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool) # string harus angka
data_str = str(data_bool) # string harus angka
data_float = float(data_bool) # false jika string kosong
print("data = ", data_int, ", type =",type(data_float))
print("data = ", data_str, ", type =",type(data_str))
print("data = ", data_float, ", type =",type(data_float))