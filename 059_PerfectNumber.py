# 完数
# 【问题】一个数如果恰好等于它的因子（即除了自身以外的约数）之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

print('1000以内的完数有：')
count = 0
for i in range(1,1000):
    i_lst = []
    for j in range(1,i):
        if i % j == 0:
            i_lst.append(j)
    if i == sum(i_lst):
        print(i,'= ',end='')
        for k in i_lst:
            print(k, end='')
            if k != i_lst[-1]:
                print(' + ',end='')
        count += 1
        print()
    
print('共有%d个' % count)
