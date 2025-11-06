from math import sqrt
print("===Chương trình tính và xuất độ dài đoạn AB")

xA = float(input('Nhập hoành độ xA: '))
xB = float(input('Nhập hoành độ xB: '))
yA = float(input('Nhập tung độ yA: '))
yB = float(input('Nhập tung độ yB: '))

AB = sqrt((xB - xA)**2 + (yB - yA)**2)  

print('Độ dài đoạn AB là = ', AB)