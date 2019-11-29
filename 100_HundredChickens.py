# 100_HundredChickens.py
# 百鸡百钱
# 【问题】我国古代数学家张丘建在《张丘建算经》一书中提出了“百鸡问题”：
# 鸡翁一，值钱五，鸡母一，值钱三，鸡雏三，值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 这个问题的大致意思是这样的：公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱。如果用100文钱买100只鸡，那么公鸡、母鸡和小鸡各应该买多少只呢？

p_cock = 5
p_hen = 3
p_chick = (1/3)
for c in range(101):
    for h in range(101-c):
        chi = 100 - c - h
        if p_cock * c + p_hen * h + p_chick * chi == 100:
            print('公鸡%d只，母鸡%d只，小鸡%d只' % (c, h, chi))
print('end')


# 参考答案
def fun():
    for i in range(0, 100, 3): # i 母鸡总价
        for j in range(0,100,5): # j 公鸡总价
            s = 100 - i - j # s 小鸡总价
            if s >= 0 and s*3 + i//3 + j//5 == 100: # 判断鸡的数量等于100
                print ('小鸡%d只，母鸡%d只，公鸡%d只'%(s*3, i//3, j//5))

fun()
