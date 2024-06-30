# Program tebak angka sederhana

import random

# Batas angka acak
min_angka = 1
max_angka = 10

# Generate angka acak
angka_tebakan = random.randint(min_angka, max_angka)

# Uji coba menebak angka
tebakan = 0
while True:
  try:
    tebakan = int(input(f"Tebak angka antara {min_angka} dan {max_angka}: "))
    if tebakan < min_angka or tebakan > max_angka:
      raise ValueError(f"Angka tebakan harus antara {min_angka} dan {max_angka}.")
    break
  except ValueError as e:
    print(f"Error: {e}")

# Menilai tebakan
if tebakan == angka_tebakan:
  print("Selamat! Tebakan kamu benar.")
else:
  print(f"Sayang sekali, tebakan kamu salah. Angka yang benar adalah {angka_tebakan}.")

