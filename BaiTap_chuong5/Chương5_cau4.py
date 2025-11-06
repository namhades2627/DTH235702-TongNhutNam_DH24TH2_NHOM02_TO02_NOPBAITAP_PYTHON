print('Câu 4: Các hàm quan trọng trong xử lý chuỗi của Python')
s = input("Nhập chuỗi: ")

hoa = thuong = so = dac_biet = khoang_trang = nguyen_am = phu_am = 0
nguyen_am_set = "AEIOUaeiou"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1

    if ch.isdigit():
        so += 1
    elif not ch.isalnum() and not ch.isspace():
        dac_biet += 1

    if ch.isspace():
        khoang_trang += 1

    if ch.isalpha():
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

print("------ Kết quả ------")
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số chữ là ký tự đặc biệt:", dac_biet)
print("Số chữ là khoảng trắng:", khoang_trang)
print("Số chữ Nguyên Âm:", nguyen_am)
print("Số chữ Phụ Âm:", phu_am)