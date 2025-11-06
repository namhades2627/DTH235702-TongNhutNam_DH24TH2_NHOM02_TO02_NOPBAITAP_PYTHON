print('Câu 3: Xử lý List Đa chiều')
from random import randrange 
 
def TaoMaTran(m, n): 
    D = [] 
    for i in range(m): 
        row = [] 
        for j in range(n): 
            row.append(randrange(100)) 
        D.append(row) 
    return D 

def XuatMaTran(D): 
    for row in D: 
        for element in row: 
            print(element, end='\t') 
        print() 

def LayDong(D, r): 
    return D[r] 

def XuatList1Chieu(R): 
    for element in R: 
        print(element, end='\t') 
    print()

def LayCot(D, c): 
    C = [] 
    for i in range(len(D)): 
        C.append(D[i][c]) 
    return C 

def MAX(D): 
    max_val = D[0][0] 
    for i in range(len(D)): 
        for j in range(len(D[i])): 
            if max_val < D[i][j]: 
                max_val = D[i][j] 
    return max_val

# Main chương trình
print("Nhập số dòng:") 
m = int(input()) 
print("Nhập số cột:") 
n = int(input()) 
D = TaoMaTran(m, n) 

print("\nMa trận ngẫu nhiên:")
XuatMaTran(D) 

print("Mời bạn nhập dòng muốn xuất:") 
r = int(input()) 
XuatList1Chieu(LayDong(D, r)) 

print("Mời bạn nhập cột muốn xuất:") 
c = int(input()) 
XuatList1Chieu(LayCot(D, c)) 

max_val = MAX(D) 
print("\nSố lớn nhất trong ma trận =", max_val)