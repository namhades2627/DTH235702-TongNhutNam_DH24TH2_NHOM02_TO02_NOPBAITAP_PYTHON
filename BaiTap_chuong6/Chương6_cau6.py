print('Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU')
from random import randrange
n = int(input("Nhập số phần tử N: "))
lst = []    
while len(lst) < n:
    num = randrange(0, 100)
    if num not in lst:
        lst.append(num)
print("List ngẫu nhiên không trùng nhau là:")
print(lst)