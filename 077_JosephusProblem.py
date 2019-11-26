## 约瑟夫生者死者小游戏
## 【问题】30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。
## 报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

def outing(p_list, outlst):
    n_l = len(p_list)
    i = n_l % 9   # 最后一个报9后剩余人数，折到队伍前面
    j = n_l // 9  # 一圈淘汰多少人
    for pp in range(n_l):
        if (pp+1) % 9 == 0:
            outlst.append(p_list[pp])
            p_list[pp] = 0
    while True:
        if 0 not in p_list:
            break
        else:
            p_list.remove(0)
    if i != 0:
        for ii in range(i):
            p_list.insert(0 ,p_list[-1])
            p_list.pop()
    if len(p_list) > 15:
        outing(p_list, outlst)
    else:
        print('被淘汰的编号有：（按淘汰顺序）', outlst) 
    
def nine_out(n):
    p_list = []
    outlst = []
    for p in range(n):
        p_list.append('p'+str(p+1))
    outing(p_list, outlst)
    
nine_out(30)


# 参考答案
people={}
for x in range(1,31):
    people[x]=1
# print(people)
check=0
i=1
j=0
while i<=31:
    if i == 31:
        i=1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue
