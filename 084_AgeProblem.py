# 年龄问题
# 【问题】王二、张三、李四、刘五年龄成一等差数列，他们四人的年龄相加是28，相乘是585。求以他们的年龄.
n1 = 0
sum_age = 28
for i in range(7):
    n4 = (sum_age * 2) / 4 - n1
    gap = (n4 - n1) / 3
    n2 = n1 + gap
    n3 = n2 + gap
    if n1 * n2 * n3 * n4 == 585:
        break
    else:
        n1 += 1
print('王二%d岁\n张三%d岁\n李四%d岁\n刘五%d岁' % (n1,n2,n3,n4))
