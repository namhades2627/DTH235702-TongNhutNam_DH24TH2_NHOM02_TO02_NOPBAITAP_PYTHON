print('Câu 13: Kiểm tra số hoàn thiện, số thịnh vượng')
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):   
        if n % i == 0:
            tong += i
    return tong

def la_so_hoan_thien(n):
    return tong_uoc_so(n) == n
def la_so_thinh_vuong(n):
    return tong_uoc_so(n) > n

n = int(input("Nhập số nguyên dương n: "))

if la_so_hoan_thien(n):
    print(f"{n} là số hoàn thiện")
elif la_so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng")
else:
    print(f"{n} không phải số hoàn thiện, cũng không phải số thịnh vượng")