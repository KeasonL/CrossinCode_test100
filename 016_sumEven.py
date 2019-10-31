## 【问题】统计 1 到 100 的偶数之和。
sum_e = 0
for i in range(101):
    if (i % 2) == 0:
        sum_e += i
print(sum_e)
