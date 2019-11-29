# 平方回文素数
# 【问题】素数的平方是回文，比如11 * 11=121。求不超过1000的平方回文素数

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


for i in range(4,1000):
    if isPrime(i):
        ss = i ** 2
        if str(ss) == str(ss)[::-1]:
            print('%s x %s = %s' %(i, i, ss))
print('end')
