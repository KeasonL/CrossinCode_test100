## 【问题】判断输入数字是否为质数
## 【分析】一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数.

# 参考了质数的规律判断法，质数与6相邻
from math import sqrt
def isPrime(n):
    if n == 1:
        return False
    if n in [2, 3]:
        return True
    if n % 6 != 1 and n % 6 !=5:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(5, sqrt_n+1):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

n = int(input('请输入一个整数：'))
if isPrime(n) == False:
    print('%d 不是质数' % n)
else:
    print('%d 是质数' % n)
