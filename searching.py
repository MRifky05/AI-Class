
# Daftar A dan nilai x yang ingin dicari
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
x = int(input("Masukkan Nilai x:2"))

# Menghitung kemunculan x dalam A
kemunculan = A.count(x)

# Mendapatkan semua indeks di mana x muncul dalam A
indeks_kemunculan = [i for i, nilai in enumerate(A) if nilai == x]

# Menampilkan hasil
print("Kemunculan x:", kemunculan)
print("Indeks kemunculan x:", indeks_kemunculan)
