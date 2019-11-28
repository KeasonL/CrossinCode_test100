# 黑洞数
# 【问题】黑洞数又称陷阱数，是类具有奇特转换特性的整数。
# 任何一个数字不全相同的整数，经有限“重排求差”操作，总会得到某一个或一些数，这些数即为黑洞数。
#“重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
# 举个例子，3位数的黑洞数为495.简易推导过程：随便找个数，如297,3个位上的数从小到大和从大到小各排一次，为972和279，相减得693。
# 按上面做法再做一次，得到594，再做一次，得到495，之后反复都得到495。验证4位数的黑洞数为6174。

import random

def findBlackHoleNum(n):
    n_lst = list(range(10))
    for q in range(len(n_lst)):
        n_lst[q] = str(n_lst[q])
    ori_num = random.sample(n_lst,n)
    gap_lst = []
    gap_repeat = 0
    print('找出%d位数的黑洞数' % n)
    print('Max\tMin\tGap')
    while True:
        nlst_min = sorted(ori_num)
        nlst_max = sorted(ori_num, reverse=True)
        n_min = int(''.join(nlst_min))
        n_max = int(''.join(nlst_max))
        gap = n_max - n_min
        print('%s\t%s\t%s' % (n_max, n_min, gap))
        if gap in gap_lst:
            gap_repeat += 1
        gap_lst.append(gap)
        ori_num = []
        for n in str(gap):
            ori_num.append(n)
        if gap_repeat == 5:
            print('Black Hole Number is %d' % gap)
            break

findBlackHoleNum(3)
findBlackHoleNum(4)
findBlackHoleNum(7)
print('end')


# 参考答案
from functools import reduce
def fun(n):
    a = [int(c) for c in str(n)]
    a.sort()
 
    s1 = reduce(lambda x, y: 10 * x + y, a[::-1])
    s2 = reduce(lambda x, y: 10 * x + y, a)
 
    return n if s1 - s2 == n else fun(s1 - s2)
 
res = fun(6294)
print('res : ', res)
