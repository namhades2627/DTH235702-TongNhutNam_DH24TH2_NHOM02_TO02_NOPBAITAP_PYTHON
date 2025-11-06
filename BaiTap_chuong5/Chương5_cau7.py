print('Câu 7: Tối ưu chuỗi danh từ')
def toi_uu_chuoi(s):
    tu = s.strip().split()
    tu = [word.capitalize() for word in tu]
    return " ".join(tu)
s = "    Tống    Nhựt    Nam   "
print("Chuỗi gốc:", repr(s))
print("Chuỗi tối ưu:", toi_uu_chuoi(s))