# 数字组合问题
## 【问题】有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

result = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and k != j:
                x = i * 100 + j * 10 + k
                print(x)
                result.append(x)

print('共有%d个这样的数' % len(result))



# 参考方法
#方法一：调用itertools获取组合的全部情况
from itertools import permutations
#从4个数中选3个数出来组合的全部情况：
lst=list(permutations(['1','2','3','4'],3))
result=''
for n in lst:
    result+=''.join(n)+'  '
print('从1,2,3,4个数中选3个数出来组合一共%s种情况\n具体组合为：%s'%(len(lst),result))

# #方法二：使用集合set()去重
lst=['1','2','3','4']
count=0
result=''
for i in lst:
    for j in lst:
        for k in lst:
            if len(set(i+j+k))==3:
                result+='%s%s%s  '%(i,j,k)
                count+=1
print('从1,2,3,4个数中选3个数出来组合一共%s种情况。\n具体组合为：%s'%(count,result))
