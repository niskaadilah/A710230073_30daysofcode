bulan1 = ['januari','februari','maret','april','mei','juni']
bulan2 = ['juli','agustus','september','oktober','november','desember']
print('Jumlah elemen pada list bulan1 : ', len(bulan1))
tahun = bulan1 + bulan2
print('Jumlah elemen pada list tahun : ', len(tahun))
print(tahun)
print(tahun[2:5])
print(tahun[:6])
print(tahun[8:])
del tahun[2]
tahun.remove('desember')
print(tahun)
tahun.insert(2,'maret')
tahun.append('desember')
print(tahun)
tahun.reverse()
print(tahun)