data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

print("Data:", data)
print("NIM :", data[1])
print("NAMA :", data[0])
print("ALAMAT :", data[2])
print("NIM:", tuple(data[1]))

nama_depan = tuple(data[0].split()[0].lower())
print("NAMA DEPAN:", nama_depan)
print("NAMA TERBALIK:", tuple(data[0].split()[::-1]))
