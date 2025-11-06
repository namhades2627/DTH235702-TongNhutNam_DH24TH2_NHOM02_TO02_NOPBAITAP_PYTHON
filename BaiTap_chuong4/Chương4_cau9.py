print("Chương trình tính căn bậc 2 lồng nhau")

from math import sqrt
n = int(input("Nhập n (số lần lồng căn): "))

S = 0
for i in range(n):
    S = sqrt(2 + S)

print(f"S({n}) = {S}")