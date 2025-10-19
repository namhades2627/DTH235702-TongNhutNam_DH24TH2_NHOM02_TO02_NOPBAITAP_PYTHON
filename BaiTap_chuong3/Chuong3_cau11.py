print('Chương trình kiểm tra số nguyên tố')
while True:
    n=int(input("Nhập 1 số nguyên dương"))
    dem=0
    for i in range(1,n+1):
        if n % i ==0 :
            dem=dem+1
    if dem==2:
        print(f"{n} là số nguyên tố")
    else :
        print(f"{n} không phải là số nguyên tố")
    hoi= input("Bạn có muốn tiếp tục không (c/k)? ")
    if hoi.lower() == 'k':
        break
print('Kết thúc chương trình!')