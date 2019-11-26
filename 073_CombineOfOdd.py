## 奇数组合问题
## 【问题】求 0~7 这 8 个数字所能组成的奇数个数。
## 数字可不全用，但不可重复

from itertools import permutations # 全排列
k = 8
total_lst = []
n_lst = list(range(k))
for q in range(len(n_lst)):
    n_lst[q] = str(n_lst[q])

for i in range(1,k+1):
    lst = list(permutations(n_lst,i))
    for j in lst:
        s = ''.join(j)
        n_s = int(s)
        if s[0] != '0' and n_s % 2 != 0:
            total_lst.append(n_s)
print('奇数个数总计%d个' % len(total_lst))
print(total_lst)


# 参考答案
sum = 4
s = 4
for j in range(2,9):
    if j <= 2:
        s *= 6
    else:
        s *= (9-j)
    print(j,s,sum)
    sum += s
print('sum = %d' % sum)
