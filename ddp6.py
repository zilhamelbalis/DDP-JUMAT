# Print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553. Pakai perulangan while. 

numbers = [
 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]

i = 0
while i < len(numbers):
    angka = numbers[i]
    if angka % 2 == 1:
        print(angka, end=" ")
    if angka == 553:
        break
    i += 1
    
print("\n=================\n")

# Buat lah output dari menggunakan bahasa pemprograman python dengan : 
# 1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 =
hasil = 0
for a in range(1,20,2):
    hasil = hasil + a
print(f"1 + 3 + 5 + 7 + 9 +11 +13 + 15 +17 +19 = {hasil}")

print("\n=================\n")

# Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini dan seterusnya sejumlah baris yang diinputkan, gunakan for loop dengan range
jumlah_baris = int(input("Masukkan jumlah baris: "))
for i in range(1, jumlah_baris + 1):
    print('*' * i)
        
        