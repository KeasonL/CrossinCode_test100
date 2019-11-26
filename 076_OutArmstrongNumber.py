## 输出阿姆斯特朗数
# 【问题】输出 1 到 10000 之间的阿姆斯特朗数。

def isArmNum(n):
    x = len(str(n))
    sum = 0
    for i in str(n):
        sum += int(i) ** x
    if sum == n:
        return True
    else:
        return False

j = 10000
print('%d以内的阿姆斯特朗数：' % j)
for k in range(1,j+1):
    if isArmNum(k):
        print(k)
