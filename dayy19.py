def hitung_luas_persegi_panjang(panjang, lebar):
  return panjang * lebar

def hitung_luas_segitiga(alas, tinggi):
  return 0.5 * alas * tinggi

def hitung_luas_lingkaran(jari_jari):
  return math.pi * jari_jari * jari_jari

def main():
  while True:
    bangun_datar = input("Masukkan jenis bangun datar (persegi panjang/segitiga/lingkaran/keluar): ")
    if bangun_datar == "persegi panjang":
      panjang = float(input("Masukkan panjang: "))
      lebar = float(input("Masukkan lebar: "))
      luas = hitung_luas_persegi_panjang(panjang, lebar)
      print(f"Luas persegi panjang: {luas}")
    elif bangun_datar == "segitiga":
      alas = float(input("Masukkan alas: "))
      tinggi = float(input("Masukkan tinggi: "))
      luas = hitung_luas_segitiga(alas, tinggi)
      print(f"Luas segitiga: {luas}")
    elif bangun_datar == "lingkaran":
      jari_jari = float(input("Masukkan jari-jari: "))
      luas = hitung_luas_lingkaran(jari_jari)
      print(f"Luas lingkaran: {luas}")
    elif bangun_datar == "keluar":
      break
    else:
      print("Bangun datar tidak valid!")

if __name__ == "__main__":
  main()
