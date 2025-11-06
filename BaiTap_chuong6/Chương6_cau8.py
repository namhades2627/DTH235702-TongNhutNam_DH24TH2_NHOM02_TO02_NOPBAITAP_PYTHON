print(' Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp'
    'dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp. ')
n = int(input("Nhập số phần tử N: "))
M = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    M.append(num)
M.sort(reverse=True)
print("Dãy số sau khi sắp xếp giảm dần là:")
print(M)