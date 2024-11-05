import numpy as np

# Definisikan matriks A, C, D, dan E
A = np.array([[3, 0], [-1, 2], [1, 1]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

print("=== Menggunakan Library (NumPy) ===")

# Perkalian A * C menggunakan NumPy
try:
    A_C = np.matmul(A, C)
    print("Hasil A * C (NumPy):")
    print(A_C)
except ValueError as e:
    print("Error perkalian A * C:", e)

# Perkalian A * D (akan menghasilkan error) menggunakan NumPy
try:
    A_D = np.matmul(A, D)
    print("Hasil A * D (NumPy):")
    print(A_D)
except ValueError as e:
    print("Error perkalian A * D:", e)

# Penjumlahan D + E menggunakan NumPy
D_plus_E = D + E
print("\nHasil D + E (NumPy):")
print(D_plus_E)

# Pengurangan D - E menggunakan NumPy
D_minus_E = D - E
print("\nHasil D - E (NumPy):")
print(D_minus_E)


print("\n=== Tanpa Menggunakan Library (Perhitungan Manual) ===")

# Definisikan matriks kembali untuk perhitungan manual
A_manual = [[3, 0], [-1, 2], [1, 1]]
C_manual = [[1, 4, 2], [3, 1, 5]]
D_manual = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E_manual = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

# Fungsi untuk perkalian matriks
def multiply_matrices(X, Y):
    # Cek apakah perkalian bisa dilakukan
    if len(X[0]) != len(Y):
        raise ValueError("Dimensi matriks tidak cocok untuk perkalian.")
    
    # Inisialisasi hasil dengan ukuran baris X x kolom Y
    result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

# Fungsi untuk penjumlahan matriks
def add_matrices(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk pengurangan matriks
def subtract_matrices(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Perkalian A * C secara manual
try:
    A_C_manual = multiply_matrices(A_manual, C_manual)
    print("Hasil A * C (Manual):")
    print(A_C_manual)
except ValueError as e:
    print("Error perkalian A * C:", e)

# Perkalian A * D secara manual (akan menghasilkan error)
try:
    A_D_manual = multiply_matrices(A_manual, D_manual)
    print("Hasil A * D (Manual):")
    print(A_D_manual)
except ValueError as e:
    print("Error perkalian A * D:", e)

# Penjumlahan D + E secara manual
D_plus_E_manual = add_matrices(D_manual, E_manual)
print("\nHasil D + E (Manual):")
print(D_plus_E_manual)

# Pengurangan D - E secara manual
D_minus_E_manual 
