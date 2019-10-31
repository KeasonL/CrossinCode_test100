## 【问题】输入数字，判断是否为偶数，是则加入列表，列表满三个元素则程序退出
n = 0
list = []
while n < 3:
    a = int(input('please input a number: '))
    if (a % 2) == 0:
        list.append(a)
        n += 1
        print('%d is an even, get it. %d number(s) in the list.' % (a,n))
    else:
        print('%d is an odd, pass' % a)
print(list)
