# 094_MersennePrime.py
# 梅森尼数
# 【问题】法国数学家梅森尼对这类形如2 ^ n-1的素数特别感兴趣，做过很多有意义的工作，后人把此类数命名为梅森尼数。
# 已经证明了，如果2 ^ n-1是素数，则幂指数n必须是素数，然而，反过来并不对，当n是素数时，2 ^ n-1不一定是素数。
# 例如，人们已经找出2 ^ 11-1是一个合数，23可以除尽它，2 ^ 23-1是一个合数，47可以除尽它。编程找出指数n在（2,50）中的梅森尼数

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

for n in range(2,50):
    if isPrime(2 ** n -1):
        print('%s = 2 ^ %s -1' % (2**n -1 , n))
print('end')
