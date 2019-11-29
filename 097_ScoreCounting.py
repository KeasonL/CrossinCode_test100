# 赛场统分
# 【问题】在编程竞赛中，有10个评委为参赛的选手打分，分数为0 ~ 100分。
# 选手最后得分为：去掉一个最高分和一个最低分后其余8个分数的平均值。请编写一个程序实现。

sc_lst = []
i = 1
while len(sc_lst) < 10:
    try:
        sc = int(input('请第%d位评委打分：' % i))
        if sc > 0 and sc < 101:
            sc_lst.append(sc)
            i += 1
        else:
            print('超出范围，输入无效')
    except:
        print('请输入1-100以内的数字')

max_sc = max(sc_lst)
min_sc = min(sc_lst)
sc_lst.remove(max_sc)
sc_lst.remove(min_sc)
ave_sc = sum(sc_lst) / len(sc_lst)
print('去除最高分%d，最低分%d，平均分为%d' % (max_sc, min_sc, ave_sc))
print('end')
