import math

#deklarasi fungsi
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'luas persegi adalah {hitung}')
    
def l_persegi_panjang(p, l):
    hitung = p * l
    print(f'luas persegi panjang adalah {hitung}')
    
def l_segitiga(alas, tinggi):
    hitung = 0.5 * alas * tinggi
    print(f'luas segitiga adalah {hitung}')
    
def l_jajar_genjang(alas, tinggi):
    hitung = alas * tinggi
    print(f'luas jajar genjang adalah {hitung}')
    
def l_lingkaran(r):
    hitung = r * 3.14 * r
    print(f'luas lingkaran adalah {hitung}')