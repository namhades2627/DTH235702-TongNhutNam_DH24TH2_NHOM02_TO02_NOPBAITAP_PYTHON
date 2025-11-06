print('Câu 10: Xử lý Ma Trận')

def nhap_ma_tran(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Nhập phần tử hàng {i}, cột {j}: ")))
        mat.append(row)
    return mat

def xuat_ma_tran(mat):
    for row in mat:
        for val in row:
            print(val, end='\t')
        print()

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def hoan_vi_ma_tran(M):
    m = len(M)
    n = len(M[0])
    H = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        H.append(row)
    return H

m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

print("Nhập ma trận A:")
A = nhap_ma_tran(m, n)

print("Nhập ma trận B:")
B = nhap_ma_tran(m, n)

print("Ma trận A:")
xuat_ma_tran(A)

print("Ma trận B:")
xuat_ma_tran(B)

print("Tổng A + B:")
C = cong_ma_tran(A, B)
xuat_ma_tran(C)

print("Hoán vị của A:")
HA = hoan_vi_ma_tran(A)
xuat_ma_tran(HA)

print("Hoán vị của B:")
HB = hoan_vi_ma_tran(B)
xuat_ma_tran(HB)