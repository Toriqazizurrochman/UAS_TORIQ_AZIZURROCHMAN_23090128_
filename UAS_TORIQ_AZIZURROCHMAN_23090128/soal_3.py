class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        """Menambahkan pesanan baru ke dalam antrian."""
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Menghapus antrian dari depan."""
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")
            return pesanan
        else:
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
            return None

    def tampilkan_antrian(self):
        """Menampilkan semua pesanan dalam antrian."""
        if len(self.antrian) > 0:
            print("Antrian saat ini:")
            for i, pesanan in enumerate(self.antrian):
                print(f"{i+1}. {pesanan}")
        else:
            print("Antrian kosong.")