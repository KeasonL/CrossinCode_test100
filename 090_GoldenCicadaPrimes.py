# 金蝉素数
# 【问题】某古寺的一块石碑上依稀刻有一些神秘的自然数。
# 专家研究发现：这些数是由1,3,5,7,9这5个奇数字排列组成的5位素数，
# 同时去掉它的最高位与最低位数字后的3位数还是素数，同时去掉它的高二位与低二位数字后的一位数还是素数。
# 因此人们把这些神秘的素数称为金蝉素数，喻意金蝉脱壳之后仍为美丽的金蝉。试求出石碑上的金蝉素数。

from itertools import permutations

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

num_lst = list(permutations([1,3,5,7,9],5))
for n_set in num_lst:
    n5 = 0
    for i in range(5):
        n5 += n_set[i] * (10**(4-i))
    if isPrime(n5):
        n3 = 0
        for k in range(1,4):
            n3 += n_set[k] * (10**(3-k))
        if isPrime(n3):
            if isPrime(n_set[2]):
                print(n5)
print('end')
