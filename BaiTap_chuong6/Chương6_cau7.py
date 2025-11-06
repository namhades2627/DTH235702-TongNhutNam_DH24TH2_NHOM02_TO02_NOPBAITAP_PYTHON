print('Câu 7: Viết chương trình nhập vào một dãy các số theo thứ  tự tăng, nếu nhập sai' 
      'quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong')
lst = []
n = int(input("Nhập số phần tử N: "))
for i in range(n):
    while True:
        num = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0 or num > lst[i-1]:
            lst.append(num)
            break
        else:
            print("Số nhập vào không hợp lệ, vui lòng nhập lại.")
print("Dãy số sau khi nhập xong là:")
print(lst)