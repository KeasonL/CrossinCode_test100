## 【问题】统计1 到 100 内质数之和
# 延续上一题的算法
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

n_sum = 0
for n in range(1,101):
    if isPrime(n):
        print(n)
        n_sum += n
print(n_sum)
