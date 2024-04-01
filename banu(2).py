class Parkiran:
    def __init__(self, k):
        self.s = k

    def parkir(self):
        if self.s:
            self.s -= 1
            print("Parkir berhasil. Slot tersisa:", self.s)
        else:
            print("Maaf, parkiran penuh.")

    def keluar(self):
        self.s += 1
        print("Anda telah keluar dari tempat parkir. Slot tersedia:", self.s)

parkiran = Parkiran(10)
print("Selamat datang di pusat perbelanjaan kami!")
parkiran.parkir()
parkiran.keluar()
print("Terima kasih telah menggunakan layanan parkir kami!")





