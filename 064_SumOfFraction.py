## 求分数序列之和
##【问题】题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

sum_fra = 0
for i in range(1,21):
    numerator = fib(i+2)
    denominator = fib(i+1)
    sum_fra += numerator / denominator
print('the sum is ', sum_fra)
