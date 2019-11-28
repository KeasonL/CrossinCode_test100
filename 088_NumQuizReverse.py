# 3位反序数
# 【问题】所谓反序数，即有这样成对的数，其特点是其中一个数的数字排列顺序完全颠倒过来，就变成另一个数，如102和201，36和63等，
# 简单的理解就是顺序相反的两个数，我们把这种成对的数互称为反序数。反序数唯一不可能出现以0结尾的数。
# 一个3位数各位上的数字都不相同，它和它的反序数的乘积是280021，这个3位数应是多少？

for i in range(1,10):
    for j in range(0,10):
        for k in range(1,10):
            if i!=k:
                n1 = i*100 + j*10 + k
                n2 = k*100 + j*10 + i
                if n1*n2 == 280021:
                    print(n1)
                    break
print('end')

for s in range(101,500):
    str_s = str(s)
    if str_s[-1] != 0:
        str_rs = str_s[::-1]
        if int(str_s) * int(str_rs) == 280021:
            print(s)
print('end')
