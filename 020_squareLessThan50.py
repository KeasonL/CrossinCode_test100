## 【问题】输入数字，如果平方运算后小于 50 则退出。
while True:
    n = float(input('please input a number:'))
    n_square = n ** 2
    if n_square < 50:
        break
    else:
        print('%.2f square is %.2f' %(n, n_square))
print('Quit')
