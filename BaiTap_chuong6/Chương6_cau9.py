def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

chuoi_dau_vao = input("Nhập vào một mảng số tự nhiên (cách nhau bằng dấu cách): ")
cac_so_dang_chuoi = chuoi_dau_vao.split()
mang_so_tu_nhien = []
for chuoi_so in cac_so_dang_chuoi:
    try:
        so = int(chuoi_so)
        mang_so_tu_nhien.append(so)
    except ValueError:
        print(f"Đã bỏ qua giá trị không phải số: '{chuoi_so}'")
print(f"Mảng bạn đã nhập là: {mang_so_tu_nhien}")
print("---")

cac_so_le = []
cac_so_chan = []
cac_so_nguyen_to = []
khong_phai_nguyen_to = []

for so in mang_so_tu_nhien:
    if so % 2 == 0:
        cac_so_chan.append(so)
    else:
        cac_so_le.append(so)

    if la_so_nguyen_to(so):
        cac_so_nguyen_to.append(so)
    else:
        khong_phai_nguyen_to.append(so)

chuoi_so_le = ", ".join([str(so) for so in cac_so_le])

print(f"Dòng 1: {chuoi_so_le}. Tổng cộng có {len(cac_so_le)} số lẻ.")

chuoi_so_chan = ", ".join([str(so) for so in cac_so_chan])
print(f"Dòng 2: {chuoi_so_chan}. Tổng cộng có {len(cac_so_chan)} số chẵn.")


chuoi_so_nguyen_to = ", ".join([str(so) for so in cac_so_nguyen_to])
print(f"Dòng 3: {chuoi_so_nguyen_to}")


chuoi_khong_nguyen_to = ", ".join([str(so) for so in khong_phai_nguyen_to])
print(f"Dòng 4: {chuoi_khong_nguyen_to}")


