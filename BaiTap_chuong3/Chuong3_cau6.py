n = int(input("Nhập số n (tối đa 2 chữ số): "))

don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if n < 10:
    print(don_vi[n])
elif n < 20:
    if n == 10:
        print("mười")
    elif n == 15:
        print("mười lăm")
    else:
        print("mười " + don_vi[n % 10])
else:
    chuc = n // 10
    dv = n % 10
    if dv == 0:
        print(hang_chuc[chuc])
    elif dv == 5:
        print(hang_chuc[chuc] + " lăm")
    else:
        print(hang_chuc[chuc] + " " + don_vi[dv])