rows = 5


for i in range(1, rows + 1):
    for j in range(1, 10):  # 2 * rows = 10
        if i + j >= 6 and j - i <= 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()


for i in range(rows + 1, 2 * rows):
    for j in range(1, 10):
        if j - i <= 4 and i + j <= 14:
            print('*', end='')
        else:
            print(' ', end='')
    print()