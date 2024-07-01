import datetime
import calendar

# Mendapatkan tanggal dan waktu saat ini
now = datetime.datetime.now()

# Mengambil komponen tanggal (tahun, bulan, hari)
tahun = now.year
bulan = now.month
hari = now.day

# Mendapatkan hari dalam seminggu (0 = Senin, 6 = Minggu)
hari_angka = calendar.weekday(tahun, bulan, hari)

# Memetakan angka hari ke nama hari
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
nama_hari_ini = nama_hari[hari_angka]

# Mendapatkan nama bulan saat ini
nama_bulan = calendar.month_name[bulan]

# Memformat string tanggal
tanggal_lengkap = f"{nama_hari_ini}, {hari} {nama_bulan} {tahun}"

# Menampilkan tanggal lengkap dan hari dalam seminggu
print(f"Hari ini adalah {tanggal_lengkap}")
