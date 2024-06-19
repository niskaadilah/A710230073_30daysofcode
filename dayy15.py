from abc import ABC, abstractmethod

class Transportasi(ABC):
    @abstractmethod
    def pesan_tiket(self, jumlah_tiket):
        pass

class Kereta(Transportasi):
    def pesan_tiket(self, jumlah_tiket):
        return f"{jumlah_tiket} tiket kereta berhasil dipesan."

class Bus(Transportasi):
    def pesan_tiket(self, jumlah_tiket):
        return f"{jumlah_tiket} tiket bus berhasil dipesan."

class Pesawat(Transportasi):
    def pesan_tiket(self, jumlah_tiket):
        return f"{jumlah_tiket} tiket pesawat berhasil dipesan."

class PemesananTiket:
    def __init__(self):
        self.transportasi = None

    def set_transportasi(self, transportasi):
        self.transportasi = transportasi

    def pesan(self, jumlah_tiket):
        if self.transportasi:
            return self.transportasi.pesan_tiket(jumlah_tiket)
        else:
            return "Transportasi belum ditentukan."

# Menggunakan polymorphism
def main():
    pemesanan = PemesananTiket()

    transportasi_kereta = Kereta()
    transportasi_bus = Bus()
    transportasi_pesawat = Pesawat()

    # Memesan tiket kereta
    pemesanan.set_transportasi(transportasi_kereta)
    print(pemesanan.pesan(3))  # Output: 3 tiket kereta berhasil dipesan.

    # Memesan tiket bus
    pemesanan.set_transportasi(transportasi_bus)
    print(pemesanan.pesan(5))  # Output: 5 tiket bus berhasil dipesan.

    # Memesan tiket pesawat
    pemesanan.set_transportasi(transportasi_pesawat)
    print(pemesanan.pesan(2))  # Output: 2 tiket pesawat berhasil dipesan.

if __name__ == "__main__":
    main()
