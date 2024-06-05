import math

def hitung_luas_keliling_lingkaran(jari_jari):
    # Menghitung luas lingkaran
    luas = math.pi * (jari_jari ** 2)
    
    # Menghitung keliling lingkaran
    keliling = 2 * math.pi * jari_jari
    
    return luas, keliling

# Contoh penggunaan
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas, keliling = hitung_luas_keliling_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {keliling:.2f}")
