from Animal import Animal

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ras, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ras = ras
        self.warna_bulu = warna_bulu
    def info_kucing(self):
        super().info_animal()
        print("Ras \t\t\t :", self.ras,
              "\nWarna bulu \t\t :", self.warna_bulu)
        

Kucing_lanang = Kucing("Lanang", "Dry Food", "Darat", "Beranak", "Anggora", "Hitam Putih")
Kucing_lanang.info_kucing()
print("=============================")
Kucing_pinky = Kucing("Pinky", "Dry Food", "Darat", "Beranak", "Domestik", "Putih")
Kucing_pinky.info_kucing()