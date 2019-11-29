## 等差素数数列
## 【问题】类似7、37、67、97、107、137、167、197，这样由素数组成的等差数列叫做等差素数数列。编程找出100以内的等差素数数列。

import time
start = time.time()

def isPrime(n):
    if n == 1:
        return False
    if n in [2, 3]:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(5, sqrt_n + 1):
        if n % i == 0 or n % ( i + 2) == 0:
            return False
    return True

plst = []
for n in range(1,100):
    if isPrime(n):
        plst.append(n)
# print(plst)

for i in range(len(plst)): 
    a0 = plst[i]
    # print('***',a0)
    for j in range(i+1,len(plst)):
        ap_lst = []
        a1 = plst[j]
        gap = a1 - a0
        a2 = a1 + gap
        if a2 in plst:
            ap_lst.append(a0)
            ap_lst.append(a1)
            while a2 in plst:
                ap_lst.append(a2)
                a2 += gap
        if len(ap_lst) > 2:
            print('gap = %d' % gap, ap_lst)

end = time.time()
print('程序运行时间：%s秒。'%(end-start))
