# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class Animal :
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
        print("Nama \t\t\t :", self.nama,
              "\nMakan \t\t\t :", self.makanan,
              "\nHidup \t\t\t :", self.hidup,
              "\nBerkembang Biak \t :", self.berkembang_biak)
        
# binatang = Animal("Kucing", "Ikan", "Darat", "Melahirkan")
# binatang.info_animal()

    