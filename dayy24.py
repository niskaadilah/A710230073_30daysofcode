# Buku Kontak Sederhana dengan Python

# Membuat kamus untuk menyimpan data kontak
kontak = {}

def tambah_kontak():
  """Fungsi untuk menambahkan kontak baru."""
  nama = input("Masukkan nama: ")
  nomor_telepon = input("Masukkan nomor telepon: ")
  email = input("Masukkan alamat email (opsional): ")

  # Menyimpan data kontak ke dalam kamus
  kontak[nama] = {
      "nomor_telepon": nomor_telepon,
      "email": email
  }

  print(f"Kontak {nama} berhasil ditambahkan!")

def tampilkan_kontak():
  """Fungsi untuk menampilkan semua kontak."""
  if not kontak:
    print("Belum ada kontak yang disimpan.")
    return

  print("Daftar Kontak:")
  for nama, data_kontak in kontak.items():
    print(f"- {nama}:")
    print(f"  Nomor Telepon: {data_kontak['nomor_telepon']}")
    if data_kontak.get("email"):
      print(f"  Email: {data_kontak['email']}")

def cari_kontak():
  """Fungsi untuk mencari kontak berdasarkan nama."""
  nama = input("Masukkan nama yang ingin dicari: ")

  if nama in kontak:
    data_kontak = kontak[nama]
    print(f"Kontak {nama}:")
    print(f"  Nomor Telepon: {data_kontak['nomor_telepon']}")
    if data_kontak.get("email"):
      print(f"  Email: {data_kontak['email']}")
  else:
    print(f"Kontak {nama} tidak ditemukan.")

def hapus_kontak():
  """Fungsi untuk menghapus kontak."""
  nama = input("Masukkan nama yang ingin dihapus: ")

  if nama in kontak:
    del kontak[nama]
    print(f"Kontak {nama} berhasil dihapus.")
  else:
    print(f"Kontak {nama} tidak ditemukan.")

while True:
  print("\nMenu Buku Kontak:")
  print("1. Tambah Kontak")
  print("2. Tampilkan Kontak")
  print("3. Cari Kontak")
  print("4. Hapus Kontak")
  print("5. Keluar")

  pilihan = input("Masukkan pilihan Anda: ")

  if pilihan == "1":
    tambah_kontak()
  elif pilihan == "2":
    tampilkan_kontak()
  elif pilihan == "3":
    cari_kontak()
  elif pilihan == "4":
    hapus_kontak()
  elif pilihan == "5":
    print("Terima kasih telah menggunakan Buku Kontak!")
    break
  else:
    print("Pilihan tidak valid. Silakan coba lagi.")
