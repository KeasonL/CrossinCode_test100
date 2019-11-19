## 杨辉三角
## 【问题】打印出杨辉三角形（要求打印出10行）。

def pascal_triangle(n):
    list_n = []
    for row in range(n):
        list_n.append([])
        for col in range(n*2-1):
            list_n[row].append(0)
            if row == 0 and col == n:
                list_n[row][col-1] = 1
            if row > 0 and row < n and col > 0 and col < (n-1)*2:
                list_n[row][col] = list_n[row-1][col-1] + list_n[row-1][col+1]
            if row == (n-1) and (col == 0 or col == (n-1)*2):
                list_n[row][col] = 1
    for r in range(len(list_n)):
        for c in range(len(list_n[r])):
            if list_n[r][c] == 0:
                list_n[r][c] = ''
            print(list_n[r][c],end='\t')
            # print(list_n[r][c],end='')
        print()
        
pascal_triangle(10)
