def hitung_rata_rata(nilai):
  """
  Fungsi untuk menghitung rata-rata nilai siswa.

  Args:
    nilai (list): Daftar nilai siswa.

  Returns:
    float: Rata-rata nilai siswa.
  """
  total = sum(nilai)
  return total / len(nilai)

def hitung_nilai_tertinggi(nilai):
  """
  Fungsi untuk mencari nilai tertinggi dalam daftar.

  Args:
    nilai (list): Daftar nilai siswa.

  Returns:
    float: Nilai tertinggi dalam daftar.
  """
  return max(nilai)

def hitung_nilai_terendah(nilai):
  """
  Fungsi untuk mencari nilai terendah dalam daftar.

  Args:
    nilai (list): Daftar nilai siswa.

  Returns:
    float: Nilai terendah dalam daftar.
  """
  return min(nilai)

def main():
  """
  Fungsi utama untuk menjalankan program.
  """
  # Meminta data dari pengguna
  jumlah_siswa = int(input("Masukkan jumlah siswa: "))
  nilai_siswa = []
  for i in range(jumlah_siswa):
    nilai = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
    nilai_siswa.append(nilai)

  # Hitung rata-rata, nilai tertinggi, dan nilai terendah
  rata_rata = hitung_rata_rata(nilai_siswa)
  nilai_tertinggi = hitung_nilai_tertinggi(nilai_siswa)
  nilai_terendah = hitung_nilai_terendah(nilai_siswa)

  # Tampilkan hasil
  print(f"Rata-rata nilai: {rata_rata}")
  print(f"Nilai tertinggi: {nilai_tertinggi}")
  print(f"Nilai terendah: {nilai_terendah}")

if __name__ == "__main__":
  main()
