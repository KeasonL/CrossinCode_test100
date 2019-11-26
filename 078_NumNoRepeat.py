## 不重复的3位数
##【问题】0 ~ 9这10个数字可以组成多少不重复的3位数？

# 列举 方法一
from itertools import permutations # 全排列
n_lst = []
for q in range(10):
    n_lst.append(str(q))

lst = list(permutations(n_lst,3))
t_lst = []
for j in lst:
    s = ''.join(j)
    if j[0] != '0':
        t_lst.append(int(s))
print('0-9可以组成 %d 个不重复的三位数' % len(t_lst))

# 列举 方法二
lst = []
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if i!=j and i!=k and j!=k:
                lst.append(i*100+j*10+k)
print('0-9可以组成 %d 个不重复的三位数' % len(t_lst))

# 数学计算 方法三
x = 9 * 9 * 8
print(x)
