## 打印菱形图案
## 【问题】打印如下菱形图案

blanklist = [3, 2, 1, 0, 1, 2, 3]
starlist = [1, 3, 5, 7, 5, 3, 1]
for i in range(7):
    print(' '*blanklist[i] + '*'*starlist[i])
