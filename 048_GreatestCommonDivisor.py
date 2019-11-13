## 【问题】任意输入两个整数求他们的最大公约数

# 辗转相除法
def getDivisor_1(max_n, min_n):
    temp = max_n % min_n
    if temp == 0:
        print('最大公约数是：%d' % min_n)
    else:
        max_n, min_n = min_n, temp
        getDivisor(max_n, min_n)

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
max_n = max([a, b])
min_n = min([a, b])
getDivisor_1(max_n, min_n)
print('END')



# 更相减损法
def getDivisor_2(max_n, min_n, d = 0):
    if (max_n % 2 == 0) and (min_n % 2 == 0):
        max_n = max_n / 2
        min_n = min_n / 2
        d += 1
        getDivisor_2(max_n, min_n, d)
    else:
        temp = max_n - min_n
        if temp == 0:
            if d == 0:
                divisor = min_n
            else:
                divisor = min_n * 2 * d
            print('最大公约数是：%d' % divisor)
        else:
            max_n = max([temp, min_n])
            min_n = min([temp, min_n])
            getDivisor_2(max_n, min_n, d)

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
max_n = max([a, b])
min_n = min([a, b])
getDivisor_2(max_n, min_n)
print('END')



# 参考答案
# 定义一个函数
def mcd(x, y):
   """该函数返回两个数的最大公约数"""
   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           mc = i
 
   return mc
 
# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
print( num1,"和", num2,"的最大公约数为", mcd(num1, num2))
