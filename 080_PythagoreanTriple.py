## 勾股数
## 【问题】所谓勾股数，一般是指能够构成直角三角形3条边的3个正整数（a,b,c)。即a2+b2=c2，a，b，cΣN。求1000以内的勾股数。
import time
start=time.time()

def pyth_triple(n):
    count = 0
    for a in range(1,n):
        for b in range(a,n):
            c = (a**2 + b**2) ** 0.5
            if c > 1000:
                break
            if c.is_integer():
                print(a,b,int(c))
                count += 1
    print('共有%d组勾股数' % count)

pyth_triple(1000)

end=time.time()
print('程序运行时间：%s秒。'%(end-start))
