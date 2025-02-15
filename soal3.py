gaji = eval (input("Gaji diinginkan per jam: "))
jumlah_waktu = eval (input("Jumlah jam kerja selama satu minggu: "))

penghasilantotal = gaji * jumlah_waktu * 5
print("Pendapatan Budi selama libur musim panas sebelum bayar pajak yaitu: Rp", penghasilantotal)

penghasilanbersih = penghasilantotal - (penghasilantotal * 0.14)
print("Pendapatan Budi setelah bayar pajak: Rp", penghasilanbersih)

pakaianaksesoris = penghasilanbersih * 0.10
print("Jumlah uang yang dihabiskan Budi untuk aksesoris yaitu: Rp", pakaianaksesoris)

alattulis = penghasilanbersih * 0.01
print("Jumlah uang yang dihabiskan Budi untuk beli alat tulis yaitu: Rp", alattulis)

sedekah = (penghasilanbersih - pakaianaksesoris - alattulis) * 0.25
print("Jumlah uang yang dihabiskan Budi untuk sedekah: Rp", sedekah)

anakyatim = ((penghasilanbersih - pakaianaksesoris - alattulis - sedekah)/1000) * 0.3
print("Jumlah uang yang diterima anak yatim yaitu: Rp", anakyatim)

dhuafa = (penghasilanbersih - pakaianaksesoris - alattulis - sedekah - anakyatim)
print("Jumlah uang yang diterima kaum dhuafa yaitu: Rp", dhuafa)