## 【问题】输出 9*9 乘法口诀表, 如下图：
##【分析】分行与列考虑，共9行9列，i控制行，j控制列。
k = 9
for i in range(1, k + 1):
    for j in range(1, i+ 1):
        print('%d*%d=%d |' %(i, j, i * j),end='')
    print('\n')
print('END')
