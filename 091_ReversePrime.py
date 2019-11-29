## 可逆素数
## 【问题】编写程序找出1 ~ 900之间的所有可逆素数（可逆素数是指一个素数的各位数值顺序颠倒后得到的数仍为素数，如113、311）。

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

lst1 = []
for i in range(1,901):
    if isPrime(i):
        lst1.append(i)
lst2 = []
for k in lst1:
    kk = int(str(k)[::-1])
    if isPrime(kk) and kk < 900:
        if kk not in lst2:
            lst2.append(k)
            print(k, kk)
print('end')
