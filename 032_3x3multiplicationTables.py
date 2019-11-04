## 【问题】请打印出 3*3 乘法口诀表。
k = 3
for i in range(1, k + 1):
    for j in range(1, k + 1):
        print('%d*%d=%d |' %(i, j, i * j),end='')
    print('\n')
print('END')
