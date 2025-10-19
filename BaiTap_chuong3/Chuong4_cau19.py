import math
def equation(x, n):
    result = 0
    for i in range(n+1):
        result+=(x**(2*i + 1))/(math.factorial(2*i + 1))
    return result

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
result = equation(x, n)
print(result)