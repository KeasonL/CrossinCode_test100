## 猴子分桃问题
## 【问题】海滩上有一堆桃子，五只猴子来分。
## 第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
## 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
## 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

last_share = 1 # 第五只猴子拿走的数量
while True:
    n = last_share * 5 + 1 # 第五只猴子来的时候有多少个桃子/第四只猴子剩下的桃子
    for i in range(4):
        n = n / 4 * 5 +1 
    if n.is_integer(): # 找整数
        n = int(n)
        print('海滩上原来最少有%s个桃子' % n)
        break
    else:
        last_share += 1

for j in range(5):
    share = (n - 1) / 5
    n -= (share + 1)
    print('第%s只猴子拿走%.f只桃子，剩下%.f只桃子' % (j+1,share,n))
    
print('End')

# 参考答案
i = 0
j = 1
x = 0
while (i < 5) :
    x = 4 * j
    for i in range(0,5) :
        if(x%4 != 0) :
            break
        else :
            i += 1
        x = (x//4) * 5 +1
    j += 1
print(x)
