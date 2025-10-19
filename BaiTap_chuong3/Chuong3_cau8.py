print("====Chương trình xuất kết quả theo phép toán đã nhập====")
pheptoan = input("Nhập phép toán (+, -, *, /): ")
try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    if pheptoan == '+':
        ketqua = a + b
    elif pheptoan == '-':
        ketqua = a - b
    elif pheptoan == '*':
        ketqua = a * b
    elif pheptoan == '/':
        if b == 0:
            print("Không thể chia cho 0")
        else:
            ketqua = a / b
            ketqua = None   
    else:
        print("Phép toán không hợp lệ")
        ketqua = None
    if ketqua is not None:
        print(f"Kết quả của {a} {pheptoan} {b} = {ketqua}")
except ValueError:
    print("Dữ liệu không hợp lệ: phải là số.")