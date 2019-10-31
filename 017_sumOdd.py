## 【问题】统计 1 到 100 奇数之和。
sum_o = 0
for i in range(101):
    if (i % 2) !=0:
        sum_o += i
print(sum_o)
