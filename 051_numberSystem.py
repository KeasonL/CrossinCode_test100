## 【问题】输入十进制数转二进制、八进制、十六进制
## 【分析】可使用 python 内置函数

n = int(input('请输入一个整数：'))
print('十进制数为：',n)
print('转换为二进制为：',bin(n))
print('转换为八进制为：',oct(n))
print('转换为十六进制为：',hex(n))

## 参考
# 几进制数 转换成 十进制数 ，都是用 int()  函数 。
# 之后后面的 第二个参数 写清楚 前面字符串 是 几进制数就可以 。
# 注意一定要合法。 比如2进制数就不能出现2这样的字符。

#十进制转为二进制
print(bin(10))

#二进制转为十进制
print(int("1000000",2))

#十进制转为八进制
print(oct(11))

#八进制转为十进制
print(int('77',8))

#十进制转为十六进制
print(hex(10))

#十六进制转为十进制
print(int('0xf',16))

# oct 函数 可将任意进制的数 转换成 8进制的。
print(oct(11))
print(oct(0b1010))
print(oct(0xf))
