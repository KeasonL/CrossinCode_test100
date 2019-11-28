# 尾数前移
# 【问题】求一个自然数N，个位数是6，将6提到最前面所得数是N的4倍。

i = 0
while True:
    n1 = i * 10 + 6
    leni = len(str(i))
    n2 = 6 * (10**leni) + i
    if n1 * 4 == n2:
        print(n1)
        break
    i += 1
print('end')
