## 【问题】任意输入两个整数,最小公倍数算法

# 辗转相除法求最大公约数
def getDivisor(n_1, n_2):
    max_n = max([n_1, n_2])
    min_n = min([n_1, n_2])
    temp = max_n % min_n
    while temp != 0:
        max_n, min_n = min_n, temp
        temp = max_n % min_n
    print('最大公约数是：%d' % min_n)
    return min_n

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
divisor =  getDivisor(a, b)
# 最小公倍数是两数之积除以最大公约数
multiple = a * b / divisor
print('最小公倍数是：%d' % multiple)
print('END')
