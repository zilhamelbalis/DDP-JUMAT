#1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)

nama, nim, kelas, noTelp, alamat = "Zilha Melbalis", "0110124026", "SI08", "0895332572882", "Cibinong, Kabupaten Bogor"
print("Nama Mahasiswa:", nama)
print("NIM:", nim)
print("Kelas:", kelas)
print("Nomor Telepon:", noTelp)
print("Alamat Mahasiswa:", alamat)

#2. Buatlah program python untuk menuliskan profil teman (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)

nama, nim, kelas, noTelp, alamat = "Eva Adawiyah", "0110124021", "SI08", "085772631836", "Cilodong, Depok"
print("Nama Mahasiswa:", nama)
print("NIM:", nim)
print("Kelas:", kelas)
print("Nomor Telepon:", noTelp)
print("Alamat Mahasiswa:", alamat)

#3. buat program python untuk mencari nilai berat badan ideal 

tb = int(input("Masukkan Tinggi Badan: "))
bbIdeal = (tb - 100) - ((tb - 100) * 0.15)
print("berat badan ideal dengan tinggi badan", tb, "adalah", bbIdeal, "kg")

#4. buat program python untuk mencari nilai konversi dari celcius ke fahreinheit

celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "derajat Celsius sama dengan", fahrenheit, "derajat fahrenheit")

#5. buat program python untuk mencari luas dan keliling tabung.

print("=====mencari luas dan keliling tabunug=====")
r = int(input("masukkan jari jari tabung"))
t = int(input("masukkan tinggi tabung"))
phi = 3.14
v = phi *r*r*t
l = 2*phi*r*(r+t)
print("volume tabung =", v)
print("luas tabung =", l)
