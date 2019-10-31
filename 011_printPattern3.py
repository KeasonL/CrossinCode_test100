## 【问题】请使用 * 打印出如下三角形
h = 5
for i in range(h, -1, -1):
    if 2 < i < h:
        print('* ', ' ' * (i - 2) , '*')
    else:
        print('* ' * i) 
