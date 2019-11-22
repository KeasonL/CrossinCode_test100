## 报 3 问题
## 【问题】有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

def outing(p_list):
    n_l = len(p_list)
    i = n_l % 3   # 最后一个报三后剩余人数，折到队伍前面
    j = n_l // 3  # 一圈淘汰多少人
    for pp in range(n_l):
        if (pp+1) % 3 == 0:
            p_list[pp] = 0
    while True:
        if 0 not in p_list:
            break
        else:
            p_list.remove(0)
    if j == 0 and i == 2:
        print('胜利者是:',p_list[1])
    if i != 0:
        for ii in range(i):
            p_list.insert(0 ,p_list[-1])
            p_list.pop()
    if j != 0:
        outing(p_list)

def three_out(n):
    p_list = []
    for p in range(n):
        p_list.append('p'+str(p+1))
    print(n,'个人一起游戏，',end='')
    outing(p_list)

    
three_out(2)
three_out(5)
# three_out(7)
three_out(11)
# three_out(12)

# 参考答案
nmax = 50
n = int(input('请输入总人数:'))
num = []
for i in range(n):
    num.append(i + 1)

i = 0
k = 0
m = 0
 
while m < n - 1:
    if num[i] != 0:
        k += 1
    if k == 3:
        num[i] = 0
        k = 0
        m += 1
    i += 1
    if i == n:
        i = 0

i = 0
while num[i] == 0: 
    i += 1
print(num[i])
