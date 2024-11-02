# 1.program menentukkan bilangan ganjil dan genap
print("## 1. program bilangan ganjil dan genap ##")
print("==========================================")

# input bilangan
bilangan = int(input('masukkan bilangan anda: '))

if bilangan % 2 == 0:
    print(bilangan, "merupakan bilangan genap")
else :
    print(bilangan, "merupakan bilangan ganjil")

# 2.program menentukkan nilai ujian
print("## 1. program menentukkan nilai ujian ##")
print("==========================================")

# Nilai
nilai_ujian = int(input('masukkan nilai anda: '))

# proses dan output 
if nilai_ujian >= 75:
    print("kamu dinyatakan lulus")
else :
    print("kamu dinyatakan tidak lulus")
    
# 3.program menentukkan usia dan status
print("## 1. program menentukkan usia dan status ##")
print("==========================================")

# input usia 
usia = int(input('masukkan usia anda: '))

# proses
if usia >= 18:
    print('kamu dewasa')
elif usia >= 13 and usia <=17:
    print("kamu remaja")
else :
    print('kamu anak-anak')
    
# 4.program memasukkan status keanggotaan
print("## 1. program memasukkan status keanggotaan ##")
print("==========================================")

status_anggota = input("""daftar keanggotaan di bawah ini
                       1.Gold 
                       2. Silver 
                       3.Bronze 
                       Masukkan pilihan kamu: """)

# proses dan output
if status_anggota == 'gold' or status_anggota == 'silver':
    print('Selamat! Anda mendapatkan diskon')
elif status_anggota == 'bronze':
    print('maaf anda tidak mendapatkan diskon')
else :
    print('masukkan status anggota dengan benar')
    
# 5.meminta pengguna untuk memasukkan jumlah pembelian
jumlah_pembelian = float(input("masukkan jumlah pembelian:" ))

# proses & output
total_harga = jumlah_pembelian * (0.9 if jumlah_pembelian > 100 else 1)
print(f'total harga setelah diskon: {total_harga: 2f}')