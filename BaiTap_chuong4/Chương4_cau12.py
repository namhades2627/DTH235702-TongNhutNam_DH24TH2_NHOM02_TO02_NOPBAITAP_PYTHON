print('Câu 12: Hàm oscillate')
def oscillate(start, end):
    for i in range(start, end + 1):
        yield i
        yield -i

# Chạy thử
for n in oscillate(-3, 5):
    print(n, end=' ')