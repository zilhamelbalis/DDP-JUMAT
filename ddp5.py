# Buat variabel list dengan vallue [namaKendaraan, jenisKendaraan, ccKendaraan, warnakendaraan dan rodaKendaraan] tambahkan dari list tersebut di belakang dengan value [hargaKendaraan, tipeKendaraan] tambahkan setelah jenis kendaraan dengan value [merkKendaraan]

kendaraan = ['hyundai creta', 'mobil', 5000, 'darkblue', 4]
print(kendaraan)

kendaraan.append('500jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'hyundai')
print(kendaraan)

# Buat program python dengan match case untuk menghitung luas bangun datar, jika pilih 1 maka menghitung luas persegi, jika pilih 2 maka menghitung lingkaran & jika pilih 3 maka menghitung segitiga, kalau pilihannya tidak ada maka ada keterangan 'salah pilih'

angka_pilihan = int(input('''masukkan pilihan:
                          1. Menghitung luas persegi
                          2. Menghitung luas lingkaran
                          3. Menghitung luas segitiga
                          '''))
match angka_pilihan:
    case 1:
        print('menghitung luas persegi')
        sisi = int(input('masukkan nilai sisi: '))
        luas_persegi = sisi ** 2
        print(f'laus persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2 ')
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14159 * (jari_jari ** 2)
        print(f"Luas lingkaran: {luas}")
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga: {luas}")
    case _:
            print("Salah pilih, silakan pilih 1, 2, atau 3.")
angka_pilihan
()