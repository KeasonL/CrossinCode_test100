# 孪生素数
# 【问题】 若两个素数之差为2，则这两个素数就是孪生素数。编写程序找出1 ~ 100之间的所有孪生素数。

def isPrime(n):
    if n in [1, 2, 3]:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(5, sqrt_n + 1):
        if n % i == 0 or n % ( i + 2) == 0:
            return False
    return True

for i in range(1,101):
    if isPrime(i):
        if isPrime(i+2):
            print('%d和%d是一对孪生素数' % (i, i+2))
print('end')
