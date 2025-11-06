from math import sqrt

print('Chương trình tính diện tích tam giác')

a = float(input('Nhập cạnh a>0: '))
b = float(input('Nhập cạnh b>0: '))
c = float(input('Nhập cạnh c>0: '))

if(a <= 0 or b <= 0 or c <= 0) or (a + b <= c or a + c <=b or b + c <= a):
    print('TAM GIÁC KHÔNG HỢP LỆ')
cv = a + b + c
p = cv / 2
dt = sqrt(p *(p - a) * (p - b) * (p - c))
print("Diện tích tam giác = ",dt)