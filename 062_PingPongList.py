## 【问题】两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
## 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

team1 = ['a', 'b', 'c']
team2 = ['x', 'y', 'z']
for p1 in team2:
    for p2 in team2:
        if p1 != p2:
            for p3 in team2:
                if (p1 != p3) and (p2 != p3):
                    if (p1 != 'x') and (p3 != 'x') and (p3 != 'z'):
                        print(team1[0], 'VS',p1)
                        print(team1[1],'VS', p2)
                        print(team1[2],'VS', p3)
                        
# 参考答案
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\t c -- %s' % (chr(i),chr(j),chr(k)))

# 借鉴
#这个题换成xyz的排列问题就好理解了，不用去理会abc,第一位不是x,最后一位不是x和z就可以了
from itertools import permutations
team1=['a','b','c']
team2=['x','y','z']

#通过permutations获取team2的全排列情况
team=list(permutations(team2,3))
for n in team:
    # 当排列的情况满足第一位不是x,最后一位不是x和z时，则是符合要求的
    if n[0]!='x'and n[2]!='x' and n[2]!='z':
        for i in range(3):
            print('%s--%s'%(team1[i],n[i]))
