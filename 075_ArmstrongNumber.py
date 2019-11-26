## 阿姆斯特朗数
##【问题】检测用户输入数字是否为阿姆斯特朗数。
## 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
## 例如1^3 + 5^3 + 3^3 = 153。1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

def isArmNum(n):
    x = len(str(n))
    sum = 0
    for i in str(n):
        sum += int(i) ** x
    if sum == n:
        return True
    else:
        return False

# print(isArmNum(153))
# print(isArmNum(1632))
# print(isArmNum(1634))

n = int(input('请输入一个数字：'))
if isArmNum(n):
    print('%d是一个阿姆斯特朗数' % n)
else:
    print('%d不是一个阿姆斯特朗数' % n)

j = 1000000
print('%d以内的阿姆斯特朗数：' % j)
for k in range(1,j+1):
    if isArmNum(k):
        print(k)


## 参考答案
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))
# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")
