print('Câu 6: Trích lọc sô âm trong chuỗi')
def NegativeNumberInStrings(s):
    so_am = []
    i = 0
    while i < len(s):
        if s[i] == '-' and i+1 < len(s) and s[i+1].isdigit():
            num = '-'
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            so_am.append(int(num))
        else:
            i += 1
    return so_am
chuoi = "abc-5xyz-12k9l--p"
print("Chuỗi:", chuoi)
print("Các số nguyên âm tìm được:", NegativeNumberInStrings(chuoi))