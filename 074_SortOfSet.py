# 数组排序
# 【问题】有一个已经排好序的数组。[1,4,6,9,13,16,19,28,40,100]。现随机生成输入一个数（1-150），要求按原来的规律将它插入数组中。
# 【分析】首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

from random import randint
ori_lst = [1,4,6,9,13,16,19,28,40,100]
num = randint(1,150)
ori_lst.append(num)
ori_lst.sort()
print('插入的数字是：%d' % num)
print('新数列为：%s' % ori_lst)


# 参考答案
a = [1,4,6,9,13,16,19,28,40,100]
print ('原始列表: %s' %a)
number = int(input("\n插入一个数字:\n"))
lena = len(a)
for i in range(lena):
    if a[0] > number:
        a.insert(0,number)
        break
    elif a[lena-1]<number:
        a.append(number)
        break
    elif i not in [0,lena-1]:
        if a[i]<= number <=a[i+1]:
            a.insert(i,number)
            break

print ('排序后列表: %s .'%a)
