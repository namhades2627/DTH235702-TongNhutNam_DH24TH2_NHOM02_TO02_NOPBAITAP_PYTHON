def ROI(dt, cp):
    return (dt - cp) / cp
def GoiYDauTu(roi):
    if roi >= 0.75:
        print('Bạn nên đầu tư')
    else:
        print('Bạn không nên đầu tư')
print('Chương trình tính ROI')
dt = int(input('Nhập doanh thu: '))
cp = int(input('Nhập chi phí: '))
roi = ROI(dt, cp)
print('Tỉ lệ ROI: ', roi)
print('==> ', GoiYDauTu(roi))