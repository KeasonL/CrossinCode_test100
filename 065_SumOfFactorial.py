## 求阶乘数之和
## 【问题】求1+2!+3!+...+20!的和。n!=1×2×3×...×n

def factorial(n):
    mul_fac = 1
    for i in range(1, n + 1):
        mul_fac *= i
    return mul_fac

sum_fac = 0
for j in range(1, 21):
    sum_fac += factorial(j)
print(sum_fac)

# 参考
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print('1! + 2! + 3! + ... + 20! = %d' % s)
