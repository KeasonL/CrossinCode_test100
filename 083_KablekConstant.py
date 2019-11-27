# 卡布列克常数
# 【问题】任意一个不是用完全相同数字组成的四位数，如果对它们的每位数字重新排序，
# 组成一个较大的数和一个较小的数，然后用较大的数减去较小数，不够四位数时补零，
# 类推下去，最后将变成一个固定的数：6174，这就是卡布列克常数。
# 例如：
# 4321-1234=3087
# 8730-378=8352
# 8532-2358=6174
# 7641-1467=6174
# 编写程序验证卡布列克常数。

import random
t = int(input('想要随机验证多少次：'))
# t=2
for tt in range(t):
    n_lst = list(range(10))
    for q in range(len(n_lst)):
        n_lst[q] = str(n_lst[q])
    ori_num = random.sample(n_lst,4)
    print('第%d次验证，随机数字为%s' % (tt+1, ori_num))
    print('Max\tMin\tGap')
    while True:
        nlst_min = sorted(ori_num)
        nlst_max = sorted(ori_num, reverse=True)
        n_min = int(''.join(nlst_min))
        n_max = int(''.join(nlst_max))
        gap = n_max - n_min
        print('%s\t%s\t%s' % (n_max, n_min, gap))
        if gap == 6174:
            print('验证成功')
            break
        ori_num = []
        for n in str(gap):
            ori_num.append(n)

print('end')
