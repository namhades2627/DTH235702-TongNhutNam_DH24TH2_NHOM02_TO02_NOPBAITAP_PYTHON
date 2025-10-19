import sys

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
except ValueError:
    print("Dữ liệu không hợp lệ: phải là số nguyên.")
    sys.exit(1)

if not (1 <= m <= 12):
    print("Tháng không hợp lệ.")
    sys.exit(1)

days_in_month = [0, 31, 29 if is_leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not (1 <= d <= days_in_month[m]):
    print("Ngày không hợp lệ cho tháng đã cho.")
    sys.exit(1)

d += 1
if d > days_in_month[m]:
    d = 1
    m += 1
    if m > 12:
        m = 1
        y += 1

print(f"Ngày kế tiếp: {d}/{m}/{y}")