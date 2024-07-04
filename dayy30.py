import random

def tanya_kabar(nama):
  """Menanyakan kabar seseorang dan melakukan interaksi yang lebih panjang."""
  print(f"Hai {nama}, bagaimana kabarmu hari ini?")
  kabar = input()

  while kabar.lower() == "baik":
    print("Senang mendengarnya! Apa yang membuatmu bahagia hari ini?")
    kabar_lanjutan = input()
    if kabar_lanjutan.lower() == "tidak ada":
      print("Oh, begitu. Semoga harimu tetap menyenangkan!")
      break
    else:
      print(f"Wah, menarik sekali! Ceritakan lebih banyak dong.")

  while kabar.lower() != "baik":
    print(f"Oh, maaf mendengarnya. Ada apa {nama}? Apa yang bisa kubantu?")
    masalah = input()
    if masalah.lower() == "tidak ada":
      print("Baiklah, kalau begitu. Semoga masalahmu segera teratasi.")
      break
    else:
      print(f"Hmm, aku mengerti. Apakah ada yang bisa kulakukan untuk membantumu?")
      saran = input()
      print(f"Baiklah, aku akan coba bantu dengan {saran}. Semangat!")
      break

# Contoh penggunaan
nama = "Budi"
tanya_kabar(nama)
