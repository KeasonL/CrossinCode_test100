## 水仙花数
## 【问题】打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
## 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
## 【分析】利用for循环控制100-999个数，每个数分解出个位，十位，百位。

def isNarNum(n):
    n_1 = n // 100
    n_2 = n % 100 // 10
    n_3 = n % 10
    sum = n_1 ** 3 + n_2 ** 3 + n_3 ** 3
    if sum == n:
        return True
    else:
        return False

print('水仙花数如下：')
count = 0
for i in range(100,1000):
    if isNarNum(i):
        print(i)
        count += 1
print('共有%d个' % count)
