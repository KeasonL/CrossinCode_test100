# 回文素数
# 【问题】所谓回文素数是指，对一个整数n从左向右和从右向左读结果值相同且是素数，即称为回文素数。求不超过1000的回文素数。
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


for i in range(9,1000):
    if isPrime(i):
        if str(i)[0] == str(i)[-1]:
            print(i)
print('end')
