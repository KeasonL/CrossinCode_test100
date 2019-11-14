## 输出素数
##【问题】判断101-200之间有多少个素数，并输出所有素数。
##【分析】指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数 

def isPrime(n):
    if n in [1, 2, 3]:
        return True
    if n % 6 != 1 and n % 6 !=5:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(5, sqrt_n+1):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

print('101-200之间的素数：')
count = 0
for i in range(101,200):
    if isPrime(i):
        print(i)
        count += 1
print('共有%d个' % count)
