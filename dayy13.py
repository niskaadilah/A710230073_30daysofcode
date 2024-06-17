class CustomError(Exception):
    # Membuat custom exception
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def cek_positif(angka):
    if angka <= 0:
        raise CustomError("Angka harus lebih besar dari nol!")
    return angka

try:
    angka = int(input("Masukkan sebuah angka positif: "))
    hasil = cek_positif(angka)
    print(f"Anda memasukkan angka positif: {hasil}")
except CustomError as e:
    # Menangani custom exception
    print(f"Terjadi kesalahan: {e.message}")
