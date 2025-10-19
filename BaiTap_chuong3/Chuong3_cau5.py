print("====Chương trình đọc số====");
'''
i, j, k = 3, 5, 7
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if i < k:
        j = i
    else:
        i = k
print(i, j, k)
'''
print('(a) i = 3, j = 5, and k = 7\n(b) i = 3, j = 7, and k = 5\n'
      '(c) i = 5, j = 3, and k = 7\n(d) i = 5, j = 7, and k = 3\n'
      '(e) i = 7, j = 3, and k = 5\n(f) i = 7, j = 5, and k = 3')
print('Kết quả:')
def temp(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if i < k:
            j = i
        else:
            i = k
    return i, j, k
array = [
    ("(a)", 3, 5, 7),
    ("(b)", 3, 7, 5),
    ("(c)", 5, 3, 7),
    ("(d)", 5, 7, 3),
    ("(e)", 7, 3, 5),
    ("(f)", 7, 5, 3),
]
for label, i, j, k in array:
    i, j, k = temp(i, j, k)
    print(f"{label} i = {i}, j = {j}, k = {k}")
