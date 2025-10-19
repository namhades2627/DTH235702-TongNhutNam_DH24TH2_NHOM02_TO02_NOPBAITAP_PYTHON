print("Xác định quý trong năm từ tháng nhập vào")
while(True):
    try:
        thang = int(input("Nhập tháng (1-12): "))
        if 1 <= thang <= 12:
            if thang in [1, 2, 3]:
                quy = 1
            elif thang in [4, 5, 6]:
                quy = 2
            elif thang in [7, 8, 9]:
                quy = 3
            else:
                quy = 4
            print(f'Tháng {thang} thuộc quý {quy} trong năm.')
            break
        else:
            print("Vui lòng nhập tháng trong khoảng từ 1 đến 12.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại!")