## 统计 1 到 100 能被三整除数之和。
sum_3s = 0
for i in range(101):
    if (i % 3) == 0:
        sum_3s += i
print(sum_3s)
