# Mendefinisikan sebuah kelas bernama 'Mahasiswa'
class Mahasiswa:
    # Konstruktor kelas, digunakan untuk inisialisasi atribut
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    
    # Metode untuk mencetak informasi mahasiswa
    def tampilkan_info(self):
        print(f'Nama: {self.nama}, NPM: {self.npm}')

# Membuat dua instance dari kelas Mahasiswa
mahasiswa1 = Mahasiswa('Andi', '12345678')
mahasiswa2 = Mahasiswa('Budi', '87654321')

# Memanggil metode tampilkan_info untuk masing-masing instance
mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
