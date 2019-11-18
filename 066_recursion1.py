## 递归问题1
## 【问题】利用递归方法求5!。

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

print('5! =', f(5))
