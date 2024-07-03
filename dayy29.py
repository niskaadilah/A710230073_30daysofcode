def main():
  # Pertanyaan dan jawaban quiz
  pertanyaan = {
    "1. Siapakah presiden pertama Indonesia?": "Soekarno",
    "2. Ibukota Indonesia saat ini adalah?": "Jakarta",
    "3. Berapa jumlah sisi pada bangun datar segitiga?": "3",
  }

  # Variabel untuk menampung skor
  skor = 0

  # Menampilkan instruksi quiz
  print("Hai Mas Bagas! Ayo main quiz kecil-kecilan!")

  # Looping untuk setiap pertanyaan
  for soal, jawaban in pertanyaan.items():
    tebakan = input(f"{soal} Jawaban: ")

    # Pengecekan jawaban
    if jawaban.lower() == tebakan.lower():
      print("Benar! ")
      skor += 1
    else:
      print("Salah!  Jawaban yang benar:", jawaban)

  # Menampilkan hasil quiz
  print("\nQuiz selesai!")
  print(f"Skor Mas Bagas: {skor}/{len(pertanyaan)}")

  # Pesan semangat sesuai skor
  if skor == len(pertanyaan):
    print("Sip! Pengetahuanmu mantap sekali!")
  elif skor > 0:
    print("Semangat belajar terus ya Mas Bagas!")
  else:
    print("Jangan patah semangat!  Tetap semangat belajar!")

if __name__ == "__main__":
  main()
