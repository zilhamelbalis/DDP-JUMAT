from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna 
        self.ukuran = ukuran
    def info_ikan(self):
        super().info_animal()
        print("Warna \t\t\t :", self.warna,
              "\nUkuran \t\t :", self.ukuran)
        
Ikan_nemo = Ikan("Nemo/Ocellaris", "Plankton", "Laut", "Bertelur", "Oren Putih", "Kecil")
Ikan_nemo.info_ikan()
print("==============================")
Ikan_dori = Ikan("Dori/Tang Biru", "Plankton", "Laut", "Bertelur", "Biru", "Sedang")
Ikan_dori.info_ikan()
