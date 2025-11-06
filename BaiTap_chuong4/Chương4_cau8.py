print("====Chương trình tính loga x====")
from math import log
a = float(input("Nhập cơ số a (a > 0 và a ≠ 1): "))
x = float(input("Nhập số x (x > 0): "))

if a > 0 and a != 1 and x > 0:
    loga_x = log(x) / log(a)
    print(f"log_{int(a)}({int(x)}) = {loga_x}")
else:
    print("Dữ liệu không hợp lệ! Yêu cầu: x > 0, a > 0 và a ≠ 1.")