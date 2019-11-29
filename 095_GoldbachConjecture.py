# 哥德巴赫猜想
# 【问题】众所周知，哥德巴赫猜想的证明是一个世界性的数学难题，至今未能完全解决。
# 我国著名数学家陈景润为哥德巴赫猜想的证明作出过杰出的贡献。
# 所谓哥德巴赫猜想是说任何一个大于2的偶数都能表示成为两个素数之和。
# 编写程序，验证指定范围内[6, 100000]哥德巴赫猜想的正确性，也就是近似证明哥德巴赫猜想。

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
for n in range(1,50001):
    if isPrime(n):
        plst.append(n)

c = 0
for i in range(3,50001):
    ii = i * 2
    for j in range(len(plst)):
        gap = ii - plst[j]
        if isPrime(gap):
            print('%d = %d + %d' %(ii, plst[j], gap))
            c += 1
            break
        if j == len(plst)-1:
            print('验证出错，%d不是两个素数之和')
    if c % 100 == 0:
        print('已验证%d个数，暂未有出错信息' % c)

print('共验证了%d个数' % c)
end = time.time()
print('程序运行时间：%s秒。'%(end-start))
