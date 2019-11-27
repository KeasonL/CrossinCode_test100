# 相亲数
# 【问题】220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284。
# 284的真因数之和为1+2+4+71+142=220。
# 毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。求100000以内的相亲数。

import time
start=time.time()

def sumFactor(n):
    sumf = 0
    k = 1
    while k < (n / k):
        if (n % k) == 0:
            sumf += (k + n // k)
        k += 1
    if k == (n / k):
        sumf += k
    return (sumf - n)

for i in range(2,100000):
    sum_i = sumFactor(i)
    sum_o = sumFactor(sum_i)
    if sum_o == i and i < sum_i:
        print('%d和%d是一对相亲数' % (i,sum_i))

end=time.time()
print('程序从运行开始到结束一共花了%s秒。'%(end-start))


# 参考答案
def sumOfFactors(k):
    p = 1
    q = k 
    s = 0
    while p < q:
        if k % p == 0:
            s += p + q 
        p += 1
        q = k / p 
 
    if k == p * q and p == q:
        s += p
 
    return s - k 
 
def fun(start, end):
    for x in range(start, end):
        y = sumOfFactors(x)
        if x < y and sumOfFactors(y) == x:
            print (x, y)

fun(2, 100000)
