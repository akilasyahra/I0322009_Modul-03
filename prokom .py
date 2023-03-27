# # membuat data base pelanggan
# pelanggan = []
# alamat = []
# nohandphone = []

# # Sub program masukan pelanggan dibuat oleh budi
# def masukpelanggan():
#     pelangganBaru = input("masukan nama pelanggan = ")
#     pelanggan.append(pelangganBaru)
#     alamatBaru = input("masukan alamat pelanggan = ")
#     alamat.append(alamatBaru)
#     nohpBaru = input("masukan nomor hp = ")
#     nohandphone.append(nohpBaru)

# # Sub program masukan pelanggan dibuat oleh fani
# tampilkandata2 = """
#     nama pelanggan      \t: {0}
#     alamat pelanggan    \t: {1}
#     no. telepon         \t: {2}
# """
# def tampilkandata():
#     for i in range(0, len(pelanggan)):
#         print(tampilkandata2.format(pelanggan[i], alamat[i], nohandphone[i]))
              

# # program utama dibuat oleh ali

# jawaban = input("apakah anda ingin memasukan data pelanggan (ya/tidak) ? ")

# while jawaban in ('ya', 'Ya'):

#     masukpelanggan()
#     jawaban = input("apakah anda ingin memasukan data pelanggan (ya/tidak) ? ")

# tampilkandata()

print("===konversi kilogram ke pound===")
print()
print("kilogram         pound")

for kg in range(0, 20):
    kg = kg + 1
    lb = 2.2
    lb = lb * kg
    print(kg, "-----------", round(lb,2))

for kg in range(0, 20):
    kg = kg + 1
    lb = 2.2
    lb = lb * kg
    print(format(kg, "<5d"), end="")
    print("-----------", format(lb,">5.2f"))

