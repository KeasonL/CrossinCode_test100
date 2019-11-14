## 【问题】第n个斐波那契数。 
## 【分析】指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
## 在数学上，斐波那契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

n = int(input('你要第几个斐波那契数? ->'))

print('=====函数=====')
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print('第%d个斐波那契数是%d' % (n, fib(n)))

print('=====while=====')
x = 3
a1 = 1
a2 = 1
a3 = 1
# print(a1)
# print(a2)
while x <= n:
    a3 = a1 + a2
    # print(a3)
    a1 = a2
    a2 = a3
    x += 1
print('第%d个斐波那契数是%d' % (n, a3))
    
print('=====for=====')
a1 = 1
a2 = 1
a3 = 1
# print(a1)
# print(a2)
try:
    for x in range(3, n+1):
        a3 = a1 + a2
        # print(a3)
        a1 = a2
        a2 = a3
    print('第%d个斐波那契数是%d' % (n, a3))
except:
    print('Error')
