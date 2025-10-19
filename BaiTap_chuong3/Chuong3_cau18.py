def graph(n, option):
    if(option == 1):
        for i in range(n):
            for j in range(n):
                if(i == 0 or i == n-1 or j == 0 or j == n-1): print("*", end=' ')
                else: print(' ', end=' ')
            print()
    elif(option == 2):
        for i in range(n):
            for j in range(n):
                if(j < n - i - 1): print(' ', end = ' ')
                else: print('*', end=' ')
            print() 
    elif(option == 3):
        for i in range(n*2 - 1):
            if(i < n):
                for j in range(n*2 - 1):
                    if(j == 0 or j == i or i == n - 1): print('*', end = ' ')
                    else: print(' ', end=' ')
                print()
            else:
                for j in range(n*2 - 1):
                    if(j < n): print(' ', end = ' ')
                    else: 
                        if(j == n*2 - 2 or j == i or i == 0): print('*', end = ' ')
                        else: print(' ', end=' ')
                print()
    print()

n = int(input("Nhap n: "))

graph(n, 1)
graph(n, 2)
graph(n, 3)