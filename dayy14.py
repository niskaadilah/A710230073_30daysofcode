class Mahasiswa:
  def __init__(self, nama, nim, umur):
    self.__nama = nama
    self.__nim = nim
    self.__umur = umur

  @property
  def nama(self):
    return self.__nama

  @nama.setter
  def nama(self, nama_baru):
    if len(nama_baru) < 3:
      raise ValueError("Nama minimal 3 karakter")
    self.__nama = nama_baru

  @property
  def nim(self):
    return self.__nim

  @nim.setter
  def nim(self, nim_baru):
    if len(nim_baru) != 10:
      raise ValueError("NIM harus 10 karakter")
    self.__nim = nim_baru

  @property
  def umur(self):
    return self.__umur

  @umur.setter
  def umur(self, umur_baru):
    if umur_baru < 17:
      raise ValueError("Umur minimal 17 tahun")
    self.__umur = umur_baru

# Buat objek mahasiswa
mahasiswa1 = Mahasiswa("Budi", "1234567890", 18)

# Akses atribut nama dengan getter
print(f"Nama: {mahasiswa1.nama}")  # Output: Nama: Budi

# Ubah atribut nama dengan setter
mahasiswa1.nama = "Andi"

# Akses atribut nama setelah diubah
print(f"Nama setelah diubah: {mahasiswa1.nama}")  # Output: Nama setelah diubah: Andi

# Coba ubah nama dengan nilai yang tidak valid
try:
  mahasiswa1.nama = "Be"
except ValueError as e:
  print(f"Error: {e}")  # Output: Error: Nama minimal 3 karakter
