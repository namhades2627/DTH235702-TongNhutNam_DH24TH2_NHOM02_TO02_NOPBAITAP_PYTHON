print("====Chương trình kiểm tra năm nhuần====");
year = int(input("Nhập năm cần kiểm tra: "));
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "là năm nhuần.");
else:
    print(year, "không phải là năm nhuần.");