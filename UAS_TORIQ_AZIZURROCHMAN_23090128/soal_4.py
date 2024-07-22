class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Buah: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

# Definisikan kelas child yaitu Mangga yang mewarisi dari kelas Buah
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"{super().information()}, Vitamin: {self.vitamin}"

mangga = Mangga("Mangga Harum Manis", "Kuning", "Manis", "Vitamin C")

print(mangga.information()) 

mangga.setNama("Mangga Manalagi")
mangga.setWarna("Hijau")
mangga.setRasa("Asam Manis")
mangga.setVitamin("Vitamin A")

print(mangga.information())