## 分糖果
## 【问题】10个小孩围城一圈分糖果，老师分给第1个小孩10块，第2个小孩2块，
# 第3个小孩8块，第4个小孩22块，第5个小孩16块，第6个小孩4块，第7个小孩10块，
# 第8个小孩6块，第9个小孩14块，第10个小孩20块。
# 然后所有的小孩同时将手中的糖分一半给右边的小孩；
# 糖块数为奇数的人可向老师要一块。问经过这样几次后大家手中的糖的块数一样多？ 每人各有多少块糖？

candy_lst = [10,2,8,22,16,4,10,6,14,20]
def candyChange(c_lst):
    c_lst2 = []
    for i in c_lst:
        c_lst2.append(int(i/2))
    c_lst2.insert(0,c_lst2[-1])
    c_lst2.pop(-1)
    # print(c_lst2)
    c_lst_n = []
    for j in range(len(c_lst)):
        c_lst_n.append(c_lst[j]/2 + c_lst2[j])
        if c_lst_n[j] % 2 != 0:
            c_lst_n[j] += 1
    # print(c_lst_n)
    return c_lst_n

print(candy_lst)
c = 0
while len(set(candy_lst)) != 1:
    candy_lst = candyChange(candy_lst)
    c += 1
print(candy_lst)
print('经过%d次变换' %c)


# 参考答案
def fun():
    s = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
    count = 0
    while not all([x == s[0] for x in s]):
        s = [(s[i-1] + s[i]) / 2 for i in range(10)]
        s = [x + x % 2 for x in s]
        count += 1
    print (count, s)
 
fun()
